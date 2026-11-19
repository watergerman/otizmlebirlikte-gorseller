"""Araştırma defteri kimliği — Reels örneği (ginepig deneyi). Kullanım: python3 defter_reel.py [stills]"""
import asyncio, os, sys, subprocess
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/claude/otizmlebirlikte-gorseller/_sablon")
import overlap
F = f"file://{HERE}/node_modules/@fontsource"
RNG = {"latin": "U+0000-00FF,U+2000-206F,U+20AC,U+2122", "latin-ext": "U+0100-024F,U+1E00-1EFF,U+2190-21FF"}
def ff(fam, pkg, weights):
    return "".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('{F}/{pkg}/files/{pkg}-{s}-{w}-normal.woff2');unicode-range:{RNG[s]}}}" for w in weights for s in RNG)
FONTS = ff("Bricolage", "instrument-sans", (400, 500, 600, 700)) + ff("Plex", "geist-mono", (400, 500, 600)) + ff("Caveat", "kalam", (400, 700))

W, H, FPS = 1080, 1920, 30
INK, RED, YEL, PAPER, MUTED = "#1E2A44", "#D2553F", "#FFE16A", "#F6F1E6", "#7C6F55"
CSS = f"""{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{background:{PAPER};font-family:'Bricolage';color:{INK};position:relative}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(#E4DCC8 1.5px,transparent 1.5px),linear-gradient(90deg,#E4DCC8 1.5px,transparent 1.5px);background-size:54px 54px;opacity:.75}}
.margin{{position:absolute;top:0;bottom:0;left:118px;width:3px;background:#E39B95}}
.w{{position:absolute;left:170px;right:120px;top:300px}}
.no{{font-family:'Plex';font-size:28px;letter-spacing:3px;color:{MUTED}}} .no b{{background:{INK};color:{PAPER};padding:4px 12px;font-weight:500;margin-right:12px}}
h1{{font-weight:700;font-size:100px;line-height:1.05;letter-spacing:-1.5px;margin-top:40px}}
h2{{font-weight:700;font-size:78px;line-height:1.07;letter-spacing:-1.2px;margin-top:34px}}
/* vurgu: kelimeye tam oturur, satıra bölünmez, soldan sağa boyanır */
.hl{{position:relative;white-space:nowrap;display:inline-block;isolation:isolate}}
.hl:before{{content:"";position:absolute;z-index:-1;left:0;right:0;bottom:.06em;height:.40em;background:{YEL};border-radius:3px;
  transform-origin:0 50%;transform:scaleX(0);animation:mk .55s ease-out var(--d,0s) both}}
@keyframes mk{{to{{transform:scaleX(1)}}}}
.hand{{font-family:'Caveat';font-weight:700;color:{RED};line-height:1.05}}
.write{{clip-path:inset(0 100% 0 0);animation:wr var(--t,1s) steps(28,end) var(--d,0s) both}}
@keyframes wr{{to{{clip-path:inset(0 0 0 0)}}}}
.up{{opacity:0;animation:up .5s ease-out var(--d,0s) both}} @keyframes up{{from{{opacity:0;transform:translateY(26px)}}to{{opacity:1;transform:none}}}}
.drop{{opacity:0;animation:dp .55s cubic-bezier(.3,1.4,.5,1) var(--d,0s) both}} @keyframes dp{{from{{opacity:0;transform:translateY(-70px) rotate(var(--r,0deg))}}to{{opacity:1;transform:rotate(var(--r,0deg))}}}}
.dr{{stroke-dasharray:var(--l);stroke-dashoffset:var(--l);animation:dr var(--t,.6s) ease-out var(--d,0s) both}} @keyframes dr{{to{{stroke-dashoffset:0}}}}
.tape{{position:absolute;width:150px;height:44px;background:rgba(255,225,106,.6);transform:rotate(-6deg)}}
.fig{{position:absolute;background:#fff;box-shadow:0 2px 0 #D9CFB8;border:2px solid {INK}}}
.it{{display:flex;gap:28px;align-items:center;margin-top:40px;font-size:44px;line-height:1.22;font-weight:500}}
.ck{{flex:0 0 66px;height:66px;border:3.5px solid {INK};border-radius:7px;position:relative}}
.ck svg{{position:absolute;left:4px;top:2px}}
.sig{{position:absolute;left:170px;bottom:330px;font-family:'Plex';font-size:24px;color:{MUTED}}} .sig b{{font-family:'Bricolage';font-weight:700;font-size:30px;color:{INK};display:block}}
"""
def gp(x, y, s=1, flip=False):
    sx = -s if flip else s
    return (f'<g transform="translate({x} {y}) scale({sx} {s})" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M-62 6 C-64 -30 -20 -44 14 -40 C40 -60 78 -44 76 -14 C80 6 60 30 20 32 C-20 36 -60 34 -62 6 Z" fill="#E7B98A"/>'
            f'<path d="M30 -50 c4 -14 18 -14 18 -2" fill="#E7B98A"/><circle cx="54" cy="-18" r="4" fill="{INK}"/>'
            f'<path d="M-40 32 v12 M-10 34 v12 M30 30 v12"/></g>')
SIG = '<div class="sig up" style="--d:.3s"><b>@otizmlebirlikte</b>Otizm Spektrum Bozukluğu Eğitimi Uzmanı</div>'
def doc(body): return f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='grid'></div><div class='margin'></div>{body}</body></html>"


# --- Kasari ve ark. (2012) sahneleri: defter_reel2.py'nin CSS ve yardımcılarıyla birlikte çalışır ---
def kid(x, y, c, s=1.0, ring=False):
    r = f'<circle cx="0" cy="-60" r="46" fill="none" stroke="{RED}" stroke-width="5" stroke-dasharray="8 8"/>' if ring else ""
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="4" stroke-linejoin="round">'
            f'<circle cx="0" cy="-60" r="22" fill="{c}"/><path d="M-32 0 Q-32 -34 0 -34 Q32 -34 32 0 Z" fill="{c}"/>{r}</g>')

def k1():
    body = (f'<div class="w"><div class="no up" style="--d:.1s"><b>DENEY 08</b>BİLİM NE DİYOR?</div>'
            f'<h1 class="up" style="--d:.35s">Otizmli çocuğu mu eğitmeli, <span class="hl" style="--d:1.4s">arkadaşlarını mı?</span></h1></div>'
            f'<div class="hand write" style="--d:2.6s;--t:.9s;position:absolute;left:170px;top:1060px;font-size:50px;transform:rotate(-4deg)">60 çocuk, 30 okul</div>')
    return 7.0, doc(body)

def k2():
    cards = [("Yalnızca çocuğa", "eğitim", 170, 700, -1.2, .9), ("Yalnızca arkadaşlarına", "eğitim", 570, 700, 1.2, 2.3),
             ("İkisine birden", "eğitim", 170, 1000, .8, 3.7), ("Hiçbiri", "olağan destek", 570, 1000, -1, 5.1)]
    html = ""
    for t, sub, x, y, r, d in cards:
        html += (f'<div class="fig drop" style="--d:{d}s;--r:{r}deg;left:{x}px;width:{360 if x == 170 else 390}px;top:{y}px;height:240px;padding:30px 28px">'
                 f'<div class="tape" style="left:110px;top:-22px"></div>'
                 f'<div style="font-weight:700;font-size:40px;line-height:1.12">{t}</div>'
                 f'<div class="hand" style="font-size:40px;margin-top:10px">{sub}</div></div>')
    body = (f'<div class="w"><div class="no up" style="--d:.1s"><b>DENEY 08</b>NASIL YAPILDI?</div>'
            f'<h2 class="up" style="--d:.3s">Çocuklar kurayla <span class="hl" style="--d:1.0s">dört gruba</span> ayrıldı</h2></div>{html}'
            f'<div class="up" style="--d:7.0s;position:absolute;left:170px;right:120px;top:1310px;font-size:36px;line-height:1.35;font-weight:500;color:#3A4560">Çocuklar 1. ile 5. sınıflar arasındaydı ve normal sınıflarda okuyordu. Eğitim 6 hafta sürdü.</div>')
    return 13.0, doc(body)

def k3():
    # sınıfın arkadaşlık ağı: önce otizmli çocuk kenarda yalnız, sonra arkadaşlar eğitilince bağlar ona uzanıyor
    G = "#C9D3E0"; A = "#E7B98A"
    peers = [(330, 900), (480, 820), (620, 920), (460, 1020), (720, 1060), (330, 1100), (600, 1180)]
    links = [(0, 1), (1, 2), (2, 3), (0, 3), (3, 4), (2, 4), (0, 5), (5, 3), (4, 6), (3, 6)]
    child = (850, 820)
    base = "".join(f'<line x1="{peers[a][0]}" y1="{peers[a][1]-20}" x2="{peers[b][0]}" y2="{peers[b][1]-20}" stroke="#9AA6B8" stroke-width="4" class="up" style="--d:{.8 + k*.08:.2f}s"/>'
                   for k, (a, b) in enumerate(links))
    new = [(2, 5.6), (1, 6.4), (4, 7.2)]
    newl = "".join(f'<line x1="{peers[a][0]}" y1="{peers[a][1]-20}" x2="{child[0]}" y2="{child[1]-55}" stroke="{RED}" stroke-width="6" stroke-linecap="round" '
                   f'class="dr" style="--l:420;--d:{d}s;--t:.6s"/>' for a, d in new)
    nodes = "".join(f'<g class="drop" style="--d:{.4 + k*.1:.2f}s">{kid(x, y, G, .8)}</g>' for k, (x, y) in enumerate(peers))
    svg = (f'<svg width="1080" height="1920" style="position:absolute;left:0;top:0">{base}{newl}{nodes}'
           f'<g class="drop" style="--d:1.6s">{kid(*child, A, .9, ring=True)}</g></svg>')
    lab = (f'<div class="hand write" style="--d:2.4s;--t:.6s;position:absolute;left:690px;top:680px;font-size:40px;transform:rotate(-3deg)">kenarda</div>'
           f'<div class="hand write" style="--d:8.0s;--t:.8s;position:absolute;left:170px;top:1260px;font-size:40px;transform:rotate(-2deg)">arkadaşları eğitilince onu da aralarına aldılar</div>')
    body = (f'<div class="w"><div class="no up" style="--d:.1s"><b>GÖZLEM</b>SINIFIN ARKADAŞLIK AĞI</div>'
            f'<h2 class="up" style="--d:.3s">Kim kiminle <span class="hl" style="--d:1.0s">arkadaş?</span></h2></div>{svg}{lab}')
    return 13.0, doc(body)

def k4():
    items = ["Sınıfta daha çok arkadaşla bağ kurdular", "Sınıf arkadaşları onları daha sık “arkadaşım” diye gösterdi",
             "Teneffüste daha az yalnız kaldılar", "Etki 3 ay sonra da sürüyordu"]
    li = ""
    for k, t in enumerate(items):
        d = 1.4 + k * 2.2
        li += (f'<div class="it up" style="--d:{d:.2f}s"><div class="ck"><svg width="60" height="60" viewBox="0 0 60 60">'
               f'<path d="M10 32 L25 46 L52 12" fill="none" stroke="{RED}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" class="dr" style="--l:70;--d:{d+.35:.2f}s;--t:.35s"/></svg></div><div>{t}</div></div>')
    note = (f'<div class="fig drop" style="--d:10.4s;--r:-1deg;left:170px;right:120px;top:1330px;padding:26px 30px"><div class="tape" style="left:-24px;top:-22px"></div>'
            f'<div class="hand write" style="--d:10.9s;--t:.5s;font-size:44px">şaşırtıcı olan</div>'
            f'<div style="font-size:32px;line-height:1.35;margin-top:6px;color:#3A4560">Yalnızca çocuğa verilen eğitim tek başına bu farkı yaratmadı.</div></div>')
    body = (f'<div class="w"><div class="no up" style="--d:.1s"><b>BULGU</b>ARKADAŞLARI EĞİTİLEN GRUPLAR</div>'
            f'<h2 class="up" style="--d:.3s">Otizmli çocuklarda <span class="hl" style="--d:.9s">ne değişti?</span></h2>{li}</div>{note}')
    return 15.0, doc(body)

def k5():
    body = (f'<div class="w"><div class="no up" style="--d:.1s"><b>SINIFTA</b>NE YAPABİLİRSİNİZ?</div>'
            f'<h2 class="up" style="--d:.3s">Sınıf arkadaşlarını da <span class="hl" style="--d:1.1s">işin içine</span> katın</h2>'
            f'<div class="up" style="--d:1.8s;font-size:40px;line-height:1.38;font-weight:500;color:#3A4560;margin-top:40px">Birkaç gönüllü öğrenciye, otizmli arkadaşlarını oyuna nasıl katabileceklerini gösterin.</div></div>'
            f'<div class="fig drop" style="--d:4.4s;--r:-1.2deg;left:170px;right:120px;top:1110px;padding:28px 32px"><div class="tape" style="left:-24px;top:-22px"></div>'
            f'<div class="hand write" style="--d:4.9s;--t:.6s;font-size:44px">Size bir sorumuz var</div>'
            f'<div style="font-size:36px;line-height:1.3;margin-top:8px;font-weight:600">Sınıfınızda buna benzer bir uygulama denediniz mi?</div></div>'
            f'<div class="up" style="--d:6.0s;position:absolute;left:170px;right:120px;top:1430px;font-family:\'Plex\';font-size:26px;color:{MUTED}">Kasari ve ark. (2012), JCPP, 53(4)</div>')
    return 11.0, doc(body)

SCENES = [k1(), k2(), k3(), k4(), k5()]

async def main(stills):
    out = f"{HERE}/out/kasari"; os.makedirs(out, exist_ok=True)
    parts, probs = [], []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": W, "height": H})
        for i, (dur, html) in enumerate(SCENES, 1):
            hp = f"{out}/s{i}.html"; open(hp, "w", encoding="utf-8").write(html)
            await pg.goto(f"file://{hp}"); await pg.evaluate("document.fonts.ready")
            await pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
            await pg.evaluate(f"document.getAnimations().forEach(a=>{{a.currentTime={dur*1000-10}}})")
            probs += await overlap.check(pg, f"s{i}")
            await pg.screenshot(path=f"{out}/s{i}-end.png")
            if stills: continue
            mp = f"{out}/s{i}.mp4"
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                                   "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", mp], stdin=subprocess.PIPE)
            for f in range(int(dur * FPS)):
                await pg.evaluate(f"document.getAnimations().forEach(a=>{{a.currentTime={f/FPS*1000}}})")
                ff.stdin.write(await pg.screenshot(type="jpeg", quality=92))
            ff.stdin.close(); ff.wait(); parts.append(mp)
        await b.close()
    if probs:
        print("\n".join(probs)); sys.exit("ÇAKIŞMA VAR")
    if stills: print("stills ok"); return
    lst = f"{out}/list.txt"; open(lst, "w").write("".join(f"file '{x}'\n" for x in parts))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", f"{out}/sessiz.mp4"], check=True)
    print("ok", f"{out}/sessiz.mp4")

asyncio.run(main("stills" in sys.argv))
