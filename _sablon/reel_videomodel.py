"""Video model Reels — hareketli şemalı 'Bilim Ne Diyor?'"""
import asyncio, sys, os
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "reels_bnd.py"), encoding="utf-8").read()
exec(_src.replace("asyncio.run(main())", ""))

A, DK, O, CR, MT, G = "#2F7F86", "#1F5C62", "#F2994A", "#FBF6EE", "#DDEFEA", "#A9B8BB"
EXTRA = f"""<style>
.dr{{stroke-dasharray:var(--l);stroke-dashoffset:var(--l);animation:dr var(--d) ease-out both}}
@keyframes dr{{to{{stroke-dashoffset:0}}}}
.fi{{opacity:0;animation:fi .5s ease-out both}} @keyframes fi{{from{{opacity:0;transform:translateY(22px)}}to{{opacity:1;transform:none}}}}
.pp{{opacity:0;transform-box:fill-box;transform-origin:center;animation:pp .45s cubic-bezier(.3,1.5,.5,1) both}}
@keyframes pp{{from{{opacity:0;transform:scale(.3)}}to{{opacity:1;transform:scale(1)}}}}
.brush{{transform-box:fill-box;transform-origin:50% 100%;animation:br .5s ease-in-out infinite alternate}}
@keyframes br{{from{{transform:translateX(-10px)}}to{{transform:translateX(10px)}}}}
.prog{{transform-box:fill-box;transform-origin:0 50%;animation:pg 3s linear both}}
@keyframes pg{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
.lab{{position:absolute;text-align:center;font-size:36px;line-height:1.2;font-weight:900;color:{DK}}}
.lab span{{display:block;font-size:26px;font-weight:800;color:{O};letter-spacing:2px;margin-bottom:6px}}
</style>"""

def kid(x, y, c, s=1.0, extra=""):
    """Basit insan figürü (baş + gövde), (x,y) gövde tabanı ortası."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle cx="0" cy="-118" r="42" fill="{c}"/>'
            f'<path d="M-62 0 Q-62 -66 0 -66 Q62 -66 62 0 Z" fill="{c}"/>{extra}</g>')

def phone(x, y, delay):
    # telefon çerçevesi + ekranda diş fırçalayan model + ilerleme çubuğu
    tb = f'<rect x="-6" y="-150" width="12" height="62" rx="5" fill="{O}" class="brush"/>'
    return (f'<g class="pp" style="animation-delay:{delay}s"><g transform="translate({x} {y})">'
            f'<rect x="-120" y="-210" width="240" height="420" rx="34" fill="{DK}"/>'
            f'<rect x="-104" y="-180" width="208" height="340" rx="16" fill="{MT}"/>'
            f'{kid(0, 120, A, .95, "")}'
            f'<g transform="translate(64 140)">{tb}</g>'
            f'<rect x="-90" y="138" width="180" height="10" rx="5" fill="#B9D6D0"/>'
            f'<rect x="-90" y="138" width="180" height="10" rx="5" fill="{O}" class="prog" style="animation-delay:{delay+.6}s;animation-iteration-count:3"/>'
            f'<path d="M-14 -44 L22 -22 L-14 0 Z" fill="#fff" opacity=".0"/>'
            f'</g></g>')

def s_loop():
    dur = 13.0
    # üç istasyon: video (üst), çocuk izler (sağ alt), çocuk dener (sol alt)
    P1, P2, P3 = (540, 800), (800, 1250), (280, 1250)
    eye = '<g transform="translate(0 -118)"><circle cx="-14" cy="-4" r="6" fill="#fff"/><circle cx="14" cy="-4" r="6" fill="#fff"/></g>'
    watch = f'<g class="pp" style="animation-delay:2.4s">{kid(P2[0], P2[1]+60, G, 1.05, eye)}</g>'
    tb2 = f'<g transform="translate(72 -110)"><rect x="-6" y="-20" width="12" height="62" rx="5" fill="{O}" class="brush"/></g>'
    do = f'<g class="pp" style="animation-delay:5.0s">{kid(P3[0], P3[1]+60, A, 1.05, tb2)}</g>'
    # oklar: video -> izleyen, izleyen -> deneyen, deneyen -> video (döngü)
    arrows = (
        f'<path d="M680 900 Q790 980 800 1060" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round" class="dr" style="--l:240;--d:.8s;animation-delay:1.8s"/>'
        f'<path d="M680 1260 L400 1260" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round" class="dr" style="--l:290;--d:.9s;animation-delay:4.2s"/>'
        f'<path d="M260 1060 Q280 960 400 900" fill="none" stroke="{G}" stroke-width="10" stroke-linecap="round" stroke-dasharray="4 26" class="fi" style="animation-delay:7.0s"/>'
        f'<path d="M800 1072 l-22 -36 l40 4 z" fill="{O}" class="fi" style="animation-delay:2.5s"/>'
        f'<path d="M392 1260 l34 -22 v44 z" fill="{O}" class="fi" style="animation-delay:5.0s"/>'
    )
    svg = f'''<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0">
{phone(*P1, .5)}{arrows}{watch}{do}</svg>'''
    labs = (f'<div class="lab fi" style="left:{P1[0]+150}px;top:{P1[1]-120}px;width:250px;text-align:left;animation-delay:1.1s"><span>1. ADIM</span>Kısa video</div>'
            f'<div class="lab fi" style="left:{P2[0]-170}px;top:{P2[1]+90}px;width:340px;animation-delay:3.0s"><span>2. ADIM</span>Çocuk izler</div>'
            f'<div class="lab fi" style="left:{P3[0]-170}px;top:{P3[1]+90}px;width:340px;animation-delay:5.6s"><span>3. ADIM</span>Kendisi dener</div>')
    note = f'<div class="fi" style="position:absolute;left:96px;right:120px;top:1500px;font-size:34px;line-height:1.35;font-weight:800;color:{DK};animation-delay:7.4s">Model bir yetişkin, bir akran ya da çocuğun kendisi olabilir.</div>'
    head = f'<div class="wrap" style="top:300px;bottom:auto;display:block"><div class="ttl up" style="animation-delay:.05s">Video model nedir?</div><div class="up" style="font-size:42px;line-height:1.25;font-weight:900;color:{DK};animation-delay:.25s">Çocuk beceriyi önce videoda izler, sonra kendisi yapar</div></div>'
    return dur, EXTRA + head + svg + labs + note

def s_meta():
    dur = 10.0
    # 23 belge ikonu ızgara hâlinde tek tek belirir, sonra sayaç
    docs = ""
    cols, w, h, gx, gy = 6, 92, 116, 140, 160
    x0, y0 = 540 - (cols * gx) / 2 + gx / 2, 720
    for i in range(23):
        cx, cy = x0 + (i % cols) * gx, y0 + (i // cols) * gy
        d = .5 + i * .12
        docs += (f'<g class="pp" style="animation-delay:{d:.2f}s"><g transform="translate({cx:.0f} {cy:.0f})">'
                 f'<path d="M{-w/2} {-h/2} h{w-28} l28 28 v{h-28} h{-w} z" fill="#fff" stroke="{A}" stroke-width="6" stroke-linejoin="round"/>'
                 f'<path d="M{w/2-28} {-h/2} v28 h28" fill="none" stroke="{A}" stroke-width="6" stroke-linejoin="round"/>'
                 f'<rect x="{-w/2+16}" y="-8" width="{w-32}" height="8" rx="4" fill="{MT}"/>'
                 f'<rect x="{-w/2+16}" y="14" width="{w-46}" height="8" rx="4" fill="{MT}"/></g></g>')
    svg = f'<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0">{docs}</svg>'
    big = (f'<div class="fi" style="position:absolute;left:96px;right:120px;top:1370px;animation-delay:3.6s">'
           f'<div style="font-size:120px;font-weight:900;color:{A};line-height:1">23 çalışma</div>'
           f'<div style="font-size:40px;line-height:1.3;font-weight:800;color:{DK};margin-top:14px">tek bir meta-analizde birleştirildi</div></div>')
    head = f'<div class="wrap" style="top:300px;bottom:auto;display:block"><div class="ttl up" style="animation-delay:.05s">İşe yarıyor mu?</div></div>'
    return dur, EXTRA + head + svg + big

SCENES = [
    s_hook("Bir beceriyi anlatmak yerine videoyla göstermek işe yarar mı?"),
    s_loop(),
    s_meta(),
    s_points("Bulgu", ["Çocuklar ve gençler videodan yeni beceriler öğrendi.",
                       "Kazanımlar zamanla korundu, farklı kişilere ve ortamlara taşındı."]),
    s_act("DENEYİN", "Diş fırçalama gibi tek bir beceriyi kısa bir videoya çekin. Birlikte izleyin, sonra birlikte deneyin.",
          "Hiç denediniz mi? Evet mi, hayır mı?", "Bellini &amp; Akullian (2007), <i>Exceptional Children</i>, 73(3)"),
]

async def run():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": W, "height": H})
        await build("r9-video-model", SCENES, pg, "stills" in sys.argv)
        await b.close()
asyncio.run(run())
