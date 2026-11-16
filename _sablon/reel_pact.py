"""PACT Reels: hareketli şemalı 'Bilim Ne Diyor?' örneği. reels_bnd.py'deki CSS ve build() kullanılır."""
import asyncio, sys, os
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "reels_bnd.py"), encoding="utf-8").read()
exec(_src.replace("asyncio.run(main())", ""))

A, DK, O, CR, MT, G = "#2F7F86", "#1F5C62", "#F2994A", "#FBF6EE", "#DDEFEA", "#A9B8BB"
EXTRA = f"""
<style>
.dr{{stroke-dasharray:var(--l);stroke-dashoffset:var(--l);animation:dr var(--d) ease-out both}}
@keyframes dr{{to{{stroke-dashoffset:0}}}}
.fi{{opacity:0;animation:fi .5s ease-out both}} @keyframes fi{{from{{opacity:0;transform:translateY(24px)}}to{{opacity:1;transform:none}}}}
.pp{{opacity:0;transform-box:fill-box;transform-origin:center;animation:pp .45s cubic-bezier(.3,1.5,.5,1) both}}
@keyframes pp{{from{{opacity:0;transform:scale(.3)}}to{{opacity:1;transform:scale(1)}}}}
.orb{{offset-path:path('M540 760 m-250 0 a250 250 0 1 0 500 0 a250 250 0 1 0 -500 0');animation:orb 2.4s linear infinite both}}
@keyframes orb{{from{{offset-distance:0%}}to{{offset-distance:100%}}}}
.st{{position:absolute;width:300px;text-align:center;font-size:36px;line-height:1.22;font-weight:900;color:{DK}}}
.st span{{display:block;font-size:26px;font-weight:800;color:{O};letter-spacing:2px;margin-bottom:6px}}
</style>"""

def person(x, y, c, s=1.0, cls="", delay=0):
    return (f'<g class="pp {cls}" style="animation-delay:{delay:.2f}s"><g transform="translate({x} {y}) scale({s})">'
            f'<circle cx="0" cy="-30" r="15" fill="{c}"/><path d="M-22 14 Q-22 -10 0 -10 Q22 -10 22 14 Z" fill="{c}"/></g></g>')

# Sahne: Deney nasıl yapıldı? (iki grup + video geri bildirim döngüsü)
def s_design():
    dur = 12.5
    # iki grup: 77 ve 75 (temsilî 10'ar figür)
    grp = ""
    for i in range(10):
        grp += person(140 + (i % 5) * 52, 580 + (i // 5) * 62, A, .9, delay=.5 + i*.04)
        grp += person(620 + (i % 5) * 52, 580 + (i // 5) * 62, G, .9, delay=.9 + i*.04)
    svg = f'''<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0">
{grp}
<text x="245" y="700" text-anchor="middle" font-size="34" font-weight="900" fill="{DK}" class="fi" style="animation-delay:1.3s">77 çocuk · PACT</text>
<text x="725" y="700" text-anchor="middle" font-size="34" font-weight="900" fill="#5B6E72" class="fi" style="animation-delay:1.5s">75 çocuk · olağan destek</text>
<circle cx="540" cy="1120" r="230" fill="none" stroke="{MT}" stroke-width="18" class="fi" style="animation-delay:2.6s"/>
<circle cx="540" cy="1120" r="230" fill="none" stroke="{A}" stroke-width="18" stroke-linecap="round" class="dr" style="--l:1446;--d:3.2s;animation-delay:3.0s" transform="rotate(-90 540 1120)"/>
</svg>'''
    steps = [("1", "Ebeveyn çocukla oynar", 540, 860, 3.0), ("2", "Oyun videoya çekilir", 820, 1120, 3.8),
             ("3", "Terapistle birlikte izlenir", 540, 1390, 4.6), ("4", "Çocuğun sinyallerine daha duyarlı olunur", 260, 1120, 5.4)]
    boxes = "".join(f'<div class="st fi" style="left:{x-150}px;top:{y-60}px;animation-delay:{d}s;background:{CR};padding:8px 0"><span>{n}. ADIM</span>{t}</div>' for n, t, x, y, d in steps)
    center = f'<div class="fi" style="position:absolute;left:390px;top:1040px;width:300px;text-align:center;animation-delay:6.6s"><div style="font-size:58px;font-weight:900;color:{A};line-height:1">12</div><div style="font-size:28px;font-weight:800;color:{DK};line-height:1.25">seans + 6 ay destek<br>evde her gün<br>20–30&nbsp;dk</div></div>'
    head = f'<div class="wrap" style="top:300px;bottom:auto;display:block"><div class="ttl up" style="animation-delay:.05s">Deney nasıl yapıldı?</div><div class="up" style="font-size:44px;font-weight:900;color:{DK};animation-delay:.25s">152 çocuk (2–4 yaş) iki gruba ayrıldı</div></div>'
    return dur, EXTRA + head + svg + boxes + center

# Sahne: zaman çizelgesi
def s_timeline():
    dur = 8.5
    pts = [(170, "2–4 yaş", "Müdahale başlar", .8), (420, "1 yıl", "Müdahale biter", 1.8), (900, "~6 yıl sonra", "121 çocuk yeniden değerlendirildi", 3.6)]
    marks = ""
    for x, top, bot, d in pts:
        marks += f'<circle cx="{x}" cy="960" r="26" fill="{O if x==900 else A}" class="pp" style="animation-delay:{d}s"/>'
    svg = f'''<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0">
<line x1="170" y1="960" x2="900" y2="960" stroke="{MT}" stroke-width="14" stroke-linecap="round"/>
<line x1="170" y1="960" x2="900" y2="960" stroke="{A}" stroke-width="14" stroke-linecap="round" class="dr" style="--l:730;--d:3.2s;animation-delay:.6s"/>
<line x1="420" y1="960" x2="900" y2="960" stroke="{G}" stroke-width="14" stroke-dasharray="4 22" stroke-linecap="round" class="fi" style="animation-delay:2.2s"/>
{marks}</svg>'''
    labels = ""
    for (x, top, bot, d), side in zip(pts, ["up", "down", "up"]):
        y = 790 if side == "up" else 1010
        al = "left" if x < 300 else ("right" if x > 800 else "center")
        lx = x - 60 if al == "left" else (x - 380 if al == "right" else x - 170)
        w = 440 if al != "center" else 340
        labels += f'<div class="fi" style="position:absolute;left:{lx}px;top:{y}px;width:{w}px;text-align:{al};animation-delay:{d+.15}s"><div style="font-size:40px;font-weight:900;color:{O if x==900 else DK}">{top}</div><div style="font-size:32px;font-weight:800;color:#4E6266;line-height:1.25">{bot}</div></div>'
    note = f'<div class="fi" style="position:absolute;left:96px;right:120px;top:1210px;font-size:36px;line-height:1.35;font-weight:800;color:{DK};animation-delay:4.6s">Çocuklar değerlendirildiğinde ortalama <span style="color:{O}">10,5 yaşındaydı</span>. Değerlendirenler hangi grupta olduklarını bilmiyordu.</div>'
    head = f'<div class="wrap" style="top:330px;bottom:auto;display:block"><div class="ttl up" style="animation-delay:.05s">Peki yıllar sonra?</div></div>'
    return dur, EXTRA + head + svg + labels + note

SCENES = [
    s_hook("Çocukla değil, ebeveynle çalışmak 6 yıl sonra fark yaratır mı?"),
    s_design(),
    s_timeline(),
    s_points("Bulgu", ["PACT grubundaki çocuklarda otizm belirtilerinin şiddeti daha düşüktü.",
                       "Çocuklar ebeveynleriyle iletişimi daha sık kendileri başlattı."]),
    s_not("Dil gelişiminde fark bulunmadı. Bu bir “tedavi” değil, belirtilerde azalma. Örneklem 152 çocuk ve bulgunun tekrarlanması gerekiyor."),
    s_act("NE YAPABİLİRSİNİZ?", "Çocuğunuzla oynarken kendinizi kısa bir videoya çekin. İzlerken onun başlattığı anları fark edin ve onları takip edin.",
          "Hiç kendi oyununuzu videoya çekip izlediniz mi?", "Pickles ve ark. (2016), <i>The Lancet</i>, 388"),
]

async def run():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": W, "height": H})
        await build("r7-pact", SCENES, pg, "stills" in sys.argv)
        await b.close()
asyncio.run(run())
