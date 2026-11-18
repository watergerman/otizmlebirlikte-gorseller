"""@otizmlebirlikte otomatik paylaşım.

_yayin/takvim.json içindeki saati gelmiş gönderileri Instagram Graph API ile yayınlar,
sonucu _yayin/yayinlanan.json'a yazar. GitHub Actions tarafından ~10 dakikada bir çalıştırılır.

Takvim öğesi:
{"id": "2026-11-19-reel", "at": "2026-11-19T17:30:00+03:00",
 "type": "REELS" | "IMAGE" | "CAROUSEL" | "STORY",
 "media": ["2026-11-19-r9-video-model/reel.mp4"],   # repo içi yollar
 "caption": "...", "first_comment": "...", "thumb_offset_ms": 3000}

Kullanım:  python _yayin/publish.py            (saati gelenleri yayınla)
           python _yayin/publish.py --check    (yalnızca hesabı ve kotayı oku)
"""
import json, os, sys, time, urllib.parse, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone

IG_USER = "17841473773803559"            # @otizmlebirlikte
API = "https://graph.facebook.com/v21.0"
REPO = "watergerman/otizmlebirlikte-gorseller"
HERE = os.path.dirname(os.path.abspath(__file__))
TAKVIM = os.path.join(HERE, "takvim.json")
YAYIN = os.path.join(HERE, "yayinlanan.json")
GEC_KALMA = timedelta(hours=3)           # bundan eski kaçırılmış gönderiyi yayınlama, raporla
TOKEN = os.environ.get("IG_TOKEN", "")


def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    url = f"{API}/{path}"
    if method == "GET":
        req = urllib.request.Request(url + "?" + data.decode())
    else:
        req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        raise RuntimeError(f"{method} {path} -> {e.code}: {body}") from None


def media_url(path, sha):
    # jsDelivr doğru Content-Type ile servis eder (video/mp4, image/jpeg); commit'e sabitlenir.
    return f"https://cdn.jsdelivr.net/gh/{REPO}@{sha}/{urllib.parse.quote(path)}"


def wait_ready(cid, limit=600):
    t0 = time.time()
    while time.time() - t0 < limit:
        st = call("GET", cid, fields="status_code,status")
        if st.get("status_code") == "FINISHED":
            return
        if st.get("status_code") in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"Medya işlenemedi: {st}")
        time.sleep(8)
    raise RuntimeError("Medya işleme zaman aşımı")


def is_video(p):
    return p.lower().endswith((".mp4", ".mov"))


def publish(item, sha):
    t, media = item["type"], item["media"]
    cap = item.get("caption", "")
    if t == "IMAGE":
        cid = call("POST", f"{IG_USER}/media", image_url=media_url(media[0], sha), caption=cap)["id"]
    elif t == "REELS":
        p = dict(media_type="REELS", video_url=media_url(media[0], sha), caption=cap, share_to_feed="true")
        if item.get("thumb_offset_ms") is not None:
            p["thumb_offset"] = str(item["thumb_offset_ms"])
        cid = call("POST", f"{IG_USER}/media", **p)["id"]
    elif t == "STORY":
        key = "video_url" if is_video(media[0]) else "image_url"
        cid = call("POST", f"{IG_USER}/media", media_type="STORIES", **{key: media_url(media[0], sha)})["id"]
    elif t == "CAROUSEL":
        kids = []
        for m in media:
            key = "video_url" if is_video(m) else "image_url"
            extra = {"media_type": "VIDEO"} if is_video(m) else {}
            k = call("POST", f"{IG_USER}/media", is_carousel_item="true", **{key: media_url(m, sha)}, **extra)["id"]
            if is_video(m):
                wait_ready(k)
            kids.append(k)
        cid = call("POST", f"{IG_USER}/media", media_type="CAROUSEL", children=",".join(kids), caption=cap)["id"]
    else:
        raise ValueError(f"Bilinmeyen tür: {t}")
    wait_ready(cid)
    mid = call("POST", f"{IG_USER}/media_publish", creation_id=cid)["id"]
    out = {"media_id": mid, "published_at": datetime.now(timezone.utc).isoformat()}
    try:
        out["permalink"] = call("GET", mid, fields="permalink").get("permalink")
    except Exception as e:
        out["permalink_error"] = str(e)[:200]
    if item.get("first_comment") and t != "STORY":
        try:
            out["comment_id"] = call("POST", f"{mid}/comments", message=item["first_comment"])["id"]
        except Exception as e:
            out["comment_error"] = str(e)[:300]
    return out


def main():
    if not TOKEN:
        sys.exit("IG_TOKEN tanımlı değil")
    if "--check" in sys.argv:
        print(call("GET", IG_USER, fields="username,followers_count,media_count"))
        print(call("GET", f"{IG_USER}/content_publishing_limit", fields="quota_usage,config"))
        return
    takvim = json.load(open(TAKVIM, encoding="utf-8"))
    yayin = json.load(open(YAYIN, encoding="utf-8")) if os.path.exists(YAYIN) else {}
    sha = os.environ.get("GITHUB_SHA") or os.popen("git rev-parse HEAD").read().strip()
    now = datetime.now(timezone.utc)
    hata = False
    for item in sorted(takvim, key=lambda x: x["at"]):
        iid = item["id"]
        if iid in yayin and "media_id" in yayin[iid]:
            continue
        at = datetime.fromisoformat(item["at"])
        if at > now:
            continue
        if now - at > GEC_KALMA:
            if iid not in yayin:
                yayin[iid] = {"skipped": "geç kaldı", "at": item["at"]}
                print(f"ATLANDI (geç): {iid}")
            continue
        tries = yayin.get(iid, {}).get("tries", 0)
        if tries >= 3:
            continue
        print(f"Yayınlanıyor: {iid} ({item['type']})")
        try:
            yayin[iid] = publish(item, sha)
            print(f"  OK {yayin[iid].get('permalink')}")
        except Exception as e:
            hata = True
            yayin[iid] = {"error": str(e)[:500], "tries": tries + 1, "at": item["at"]}
            print(f"  HATA {e}")
        json.dump(yayin, open(YAYIN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(yayin, open(YAYIN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if hata:
        sys.exit(1)


if __name__ == "__main__":
    main()
