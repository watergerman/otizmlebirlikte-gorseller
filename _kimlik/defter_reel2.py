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

def s1():
    arrow = (f'<svg width="1080" height="1920" style="position:absolute;left:0;top:0">'
             f'<path d="M470 1185 C520 1130 600 1130 650 1180" fill="none" stroke="{RED}" stroke-width="6" stroke-linecap="round" class="dr" style="--l:240;--d:2.9s"/>'
             f'<path d="M634 1156 l18 26 l-30 6" fill="none" stroke="{RED}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" class="dr" style="--l:80;--d:3.4s;--t:.3s"/>'
             f'<g class="drop" style="--d:3.6s">{gp(780, 1290, 1.3)}</g></svg>')
    body = (f'{arrow}<div class="w"><div class="no up" style="--d:.1s"><b>DENEY 07</b>BİLİM NE DİYOR?</div>'
            f'<h1 class="up" style="--d:.35s">Sınıfa küçük bir <span class="hl" style="--d:1.2s">evcil hayvan</span> gelince ne değişir?</h1></div>'
            f'<div class="hand write" style="--d:2.0s;--t:.9s;position:absolute;left:170px;top:1170px;font-size:50px;transform:rotate(-4deg)">iki ginepig,<br>10 dakika</div>')
    return 7.0, doc(body)

def s2():
    toys = (f'<svg width="310" height="250" viewBox="-155 -125 310 250"><g stroke="{INK}" stroke-width="5">'
            f'<rect x="-90" y="-10" width="60" height="60" fill="#F2A65A" class="drop" style="--d:1.3s"/><rect x="-20" y="-10" width="60" height="60" fill="#8DB7E0" class="drop" style="--d:1.45s"/>'
            f'<rect x="-55" y="-74" width="60" height="60" fill="#B9D88C" class="drop" style="--d:1.6s"/><circle cx="86" cy="22" r="30" fill="{YEL}" class="drop" style="--d:1.75s"/></g></svg>')
    pigs = f'<svg width="340" height="250" viewBox="-170 -125 340 250"><g class="drop" style="--d:4.6s">{gp(-70, 10, .85)}</g><g class="drop" style="--d:4.8s">{gp(78, 30, .75, True)}</g></svg>'
    body = (f'<div class="w"><div class="no up" style="--d:.1s"><b>DENEY 07</b>NASIL YAPILDI?</div>'
            f'<h2 class="up" style="--d:.3s">Aynı çocuklar, <span class="hl" style="--d:1.0s">iki ayrı oturum</span></h2></div>'
            f'<div class="fig drop" style="--d:.9s;--r:-1deg;left:170px;width:360px;top:800px;height:400px;padding:24px"><div class="tape" style="left:100px;top:-22px"></div>{toys}'
            f'<div class="hand write" style="--d:2.1s;--t:.6s;text-align:center;font-size:44px;margin-top:4px">oyuncaklar</div></div>'
            f'<div class="fig drop" style="--d:4.2s;--r:1.5deg;left:570px;width:390px;top:800px;height:400px;padding:24px"><div class="tape" style="left:120px;top:-22px;transform:rotate(5deg)"></div>{pigs}'
            f'<div class="hand write" style="--d:5.6s;--t:.6s;text-align:center;font-size:44px;margin-top:4px">iki ginepig</div></div>'
            f'<div class="up" style="--d:7.2s;position:absolute;left:170px;right:120px;top:1270px;font-size:38px;line-height:1.35;font-weight:500;color:#3A4560">5–12 yaş arası 33 otizmli çocuk, iki sınıf arkadaşıyla birlikte oynadı.</div>')
    return 13.0, doc(body)

def s3():
    items = ["Daha çok gülümsediler", "Yetişkinlerle daha çok konuştular", "Arkadaşları onlara daha sık yaklaştı", "Kaşlarını çatma ve ağlama azaldı"]
    li = ""
    for k, t in enumerate(items):
        d = 1.4 + k * 2.2
        li += (f'<div class="it up" style="--d:{d:.2f}s"><div class="ck"><svg width="60" height="60" viewBox="0 0 60 60">'
               f'<path d="M10 32 L25 46 L52 12" fill="none" stroke="{RED}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" class="dr" style="--l:70;--d:{d+.35:.2f}s;--t:.35s"/></svg></div><div>{t}</div></div>')
    note = (f'<div class="fig drop" style="--d:10.4s;--r:-1deg;left:170px;right:120px;top:1330px;padding:26px 30px"><div class="tape" style="left:-24px;top:-22px"></div>'
            f'<div class="hand write" style="--d:10.9s;--t:.5s;font-size:44px">ama dikkat!</div>'
            f'<div style="font-size:32px;line-height:1.35;margin-top:6px;color:#3A4560">Arkadaşlarıyla konuşma oyuncaklı oturumlarda daha fazlaydı.</div></div>')
    body = (f'<div class="w"><div class="no up" style="--d:.1s"><b>BULGU</b>GİNEPİGLER ORTAMDAYKEN</div>'
            f'<h2 class="up" style="--d:.3s">Otizmli çocuklarda <span class="hl" style="--d:.9s">ne değişti?</span></h2>{li}</div>{note}')
    return 15.0, doc(body)

def s4():
    body = (f'<div class="w"><div class="no up" style="--d:.1s"><b>SONUÇ</b>TERCİH</div></div>'
            f'<div class="up" style="--d:.5s;position:absolute;left:170px;top:560px;font-weight:700;font-size:300px;letter-spacing:-8px;line-height:1">%<span class="hl" style="--d:1.3s">82</span></div>'
            f'<div class="up" style="--d:1.0s;position:absolute;left:170px;right:120px;top:900px;font-weight:700;font-size:60px;line-height:1.12;letter-spacing:-1px">otizmli çocuk ginepigleri oyuncaklara tercih etti</div>'
            f'<div class="hand write" style="--d:3.0s;--t:.8s;position:absolute;left:170px;top:1130px;font-size:46px;transform:rotate(-3deg)">4 okul · 15 kaynaştırma sınıfı</div>'
            f'<div class="up" style="--d:4.6s;position:absolute;left:170px;right:120px;top:1290px;font-family:\'Plex\';font-size:27px;line-height:1.5;color:{MUTED}">Küçük bir çalışma: iki hayvan, çeşitli oyuncaklarla karşılaştırıldı.</div>')
    return 9.0, doc(body)

def s5():
    body = (f'<div class="w"><div class="no up" style="--d:.1s"><b>SINIFTA VE EVDE</b>NE YAPABİLİRSİNİZ?</div>'
            f'<h2 class="up" style="--d:.3s">Oyunu çocuğun <span class="hl" style="--d:1.1s">ilgisi üzerine</span> kurun</h2>'
            f'<div class="up" style="--d:1.8s;font-size:40px;line-height:1.38;font-weight:500;color:#3A4560;margin-top:40px">İlgisini çeken bir canlı ya da nesne, arkadaşlarıyla arasında doğal bir köprü olabilir.</div></div>'
            f'<div class="fig drop" style="--d:4.4s;--r:-1.2deg;left:170px;right:120px;top:1110px;padding:28px 32px"><div class="tape" style="left:-24px;top:-22px"></div>'
            f'<div class="hand write" style="--d:4.9s;--t:.6s;font-size:44px">Size bir sorumuz var</div>'
            f'<div style="font-size:36px;line-height:1.3;margin-top:8px;font-weight:600">Sınıfınızda ya da evinizde bir evcil hayvan var mı?</div></div>'
            f'<div class="up" style="--d:6.0s;position:absolute;left:170px;right:120px;top:1430px;font-family:\'Plex\';font-size:26px;color:{MUTED}">O\'Haire ve ark. (2013), PLoS ONE, 8(2)</div>')
    return 11.0, doc(body)

SCENES = [s1(), s2(), s3(), s4(), s5()]

async def main(stills):
    out = f"{HERE}/out/reel"; os.makedirs(out, exist_ok=True)
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
