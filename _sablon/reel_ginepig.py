"""Ginepig deneyi Reels — O'Haire ve ark. (2013), PLoS ONE 8(2): e57010"""
import asyncio, sys, os
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "reels_bnd.py"), encoding="utf-8").read()
exec(_src.replace("asyncio.run(main())", ""))

A, DK, O, CR, MT, G, BR = "#2F7F86", "#1F5C62", "#F2994A", "#FBF6EE", "#DDEFEA", "#A9B8BB", "#C98A4B"
EXTRA = f"""<style>
.dr{{stroke-dasharray:var(--l);stroke-dashoffset:var(--l);animation:dr var(--d) ease-out both}}
@keyframes dr{{to{{stroke-dashoffset:0}}}}
.fi{{opacity:0;animation:fi .5s ease-out both}} @keyframes fi{{from{{opacity:0;transform:translateY(22px)}}to{{opacity:1;transform:none}}}}
.pp{{opacity:0;transform-box:fill-box;transform-origin:center;animation:pp .45s cubic-bezier(.3,1.5,.5,1) both}}
@keyframes pp{{from{{opacity:0;transform:scale(.3)}}to{{opacity:1;transform:scale(1)}}}}
.bob{{transform-box:fill-box;transform-origin:center;animation:bob 1.1s ease-in-out infinite alternate}}
@keyframes bob{{from{{transform:translateY(0)}}to{{transform:translateY(-6px)}}}}
.grow{{transform-box:fill-box;transform-origin:0 50%;animation:gr .9s ease-out both}}
@keyframes gr{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
.row{{position:absolute;left:96px;right:120px;display:flex;align-items:center;gap:26px;font-size:38px;font-weight:900;color:{DK}}}
.row i{{flex:0 0 78px;height:78px;border-radius:24px;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:44px;font-weight:900}}
.row i.up{{background:{MT};color:{A}}} .row i.dn{{background:#FDECEA;color:#C2483A}}
</style>"""

def kid(x, y, c, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle cx="0" cy="-92" r="32" fill="{c}"/>'
            f'<path d="M-48 0 Q-48 -52 0 -52 Q48 -52 48 0 Z" fill="{c}"/></g>')

def gp(x, y, s=1.0, flip=False):
    sx = -s if flip else s
    return (f'<g transform="translate({x} {y}) scale({sx} {s})"><g class="bob">'
            f'<ellipse cx="0" cy="0" rx="58" ry="36" fill="{BR}"/>'
            f'<ellipse cx="-14" cy="-6" rx="24" ry="20" fill="#F4E3CF"/>'
            f'<circle cx="46" cy="-14" r="24" fill="{BR}"/>'
            f'<ellipse cx="38" cy="-36" rx="9" ry="7" fill="#A86E37"/>'
            f'<circle cx="54" cy="-18" r="4.5" fill="#2B2B2B"/>'
            f'<circle cx="68" cy="-8" r="3.5" fill="#7A4E2A"/></g></g>')

def blocks(x, y):
    return (f'<g transform="translate({x} {y})"><rect x="-56" y="-20" width="44" height="44" rx="8" fill="{O}"/>'
            f'<rect x="-6" y="-20" width="44" height="44" rx="8" fill="#7A62B5"/>'
            f'<rect x="-30" y="-66" width="44" height="44" rx="8" fill="#3F7FBF"/>'
            f'<circle cx="62" cy="4" r="22" fill="#E3B23C"/></g>')

def group(cx, cy, d0, centre):
    # bir otizmli çocuk (turuncu çerçeveli) + iki akran, ortada oyuncak/hayvan
    k = (f'<g class="pp" style="animation-delay:{d0:.2f}s">{kid(cx-150, cy+40, A)}</g>'
         f'<g class="pp" style="animation-delay:{d0+.15:.2f}s">{kid(cx, cy-70, G)}</g>'
         f'<g class="pp" style="animation-delay:{d0+.3:.2f}s">{kid(cx+150, cy+40, G)}</g>')
    return k + f'<g class="pp" style="animation-delay:{d0+.6:.2f}s">{centre}</g>'

def s_design():
    dur = 12.5
    L, R = (290, 1010), (790, 1010)
    svg = f'''<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0">
<rect x="70" y="780" width="440" height="440" rx="40" fill="#F3EDE2" class="fi" style="animation-delay:.6s"/>
<rect x="570" y="780" width="440" height="440" rx="40" fill="{MT}" class="fi" style="animation-delay:3.6s"/>
{group(L[0], L[1], .9, blocks(L[0], L[1]+90))}
{group(R[0], R[1], 3.9, gp(R[0]-110, R[1]+105, .85) + gp(R[0]+110, R[1]+105, .85, True))}
</svg>'''
    labs = (f'<div class="fi" style="position:absolute;left:70px;width:440px;top:1250px;text-align:center;animation-delay:1.8s">'
            f'<div style="font-size:38px;font-weight:900;color:#5B6E72">Oyuncaklarla</div><div style="font-size:30px;font-weight:800;color:#7A8A8D">10 dakika</div></div>'
            f'<div class="fi" style="position:absolute;left:570px;width:440px;top:1250px;text-align:center;animation-delay:4.8s">'
            f'<div style="font-size:38px;font-weight:900;color:{A}">İki ginepigle</div><div style="font-size:30px;font-weight:800;color:#7A8A8D">10 dakika</div></div>')
    note = (f'<div class="fi" style="position:absolute;left:96px;right:120px;top:1440px;font-size:34px;line-height:1.35;font-weight:800;color:{DK};animation-delay:6.4s">'
            f'Her grupta bir otizmli çocuk ve iki sınıf arkadaşı vardı. Oturumlar videoya çekildi ve iki bağımsız gözlemci tarafından puanlandı.</div>')
    head = (f'<div class="wrap" style="top:300px;bottom:auto;display:block"><div class="ttl up" style="animation-delay:.05s">Deney nasıl yapıldı?</div>'
            f'<div class="up" style="font-size:42px;line-height:1.25;font-weight:900;color:{DK};animation-delay:.25s">5–12 yaş arası 33 otizmli çocuk, sınıf arkadaşlarıyla üçlü gruplar hâlinde oynadı</div></div>')
    return dur, EXTRA + head + svg + labs + note

def s_change():
    dur = 11.0
    rows = [("up", "↑", "Daha çok gülümsediler", 1.0), ("up", "↑", "Yetişkinlerle daha çok konuştular", 2.2),
            ("up", "↑", "Arkadaşları onlara daha çok yaklaştı", 3.4), ("dn", "↓", "Kaşlarını çatma ve ağlama azaldı", 4.6)]
    html = "".join(f'<div class="row fi" style="top:{720 + k*150}px;animation-delay:{d}s"><i class="{c}">{a}</i><span>{t}</span></div>'
                   for k, (c, a, t, d) in enumerate(rows))
    small = (f'<div class="fi" style="position:absolute;left:96px;right:120px;top:1370px;font-size:30px;line-height:1.4;font-weight:700;color:#6B7B7E;animation-delay:6.4s">'
             f'Bir şaşırtıcı ayrıntı: Arkadaşlarıyla konuşma, oyuncaklı oturumlarda daha fazlaydı. Küçük bir çalışma; iki hayvan, çeşitli oyuncaklarla karşılaştırıldı.</div>')
    head = (f'<div class="wrap" style="top:300px;bottom:auto;display:block"><div class="ttl up" style="animation-delay:.05s">Ne değişti?</div>'
            f'<div class="up" style="font-size:42px;line-height:1.25;font-weight:900;color:{DK};animation-delay:.25s">Ginepigler ortamdayken otizmli çocuklar:</div></div>')
    return dur, EXTRA + head + html + small

SCENES = [
    s_hook("Sınıfa küçük bir evcil hayvan gelince otizmli çocuklarda ne değişir?"),
    s_design(),
    s_change(),
    s_stat("%82", "otizmli çocuk ginepigleri oyuncaklara tercih etti", "Avustralya'da 4 okul, 15 kaynaştırma sınıfı"),
    s_act("SINIFTA VE EVDE", "Çocuğun ilgisini çeken bir canlı ya da nesne, arkadaşlarıyla arasında doğal bir köprü olabilir. Oyunu onun ilgisi üzerine kurun.",
          "Sınıfınızda ya da evinizde bir evcil hayvan var mı? Evet mi, hayır mı?", "O'Haire ve ark. (2013), <i>PLoS ONE</i>, 8(2)"),
]

async def run():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": W, "height": H})
        await build("r9b-ginepig", SCENES, pg, "stills" in sys.argv)
        await b.close()
asyncio.run(run())
