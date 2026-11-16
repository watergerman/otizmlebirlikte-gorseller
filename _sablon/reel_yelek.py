"""Ağırlıklı yelek Reels — ABAB grafikli 'Bilim Ne Diyor?'"""
import asyncio, sys, os
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "reels_bnd.py"), encoding="utf-8").read()
exec(_src.replace("asyncio.run(main())", ""))

A, DK, O, MT, G = "#2F7F86", "#1F5C62", "#F2994A", "#DDEFEA", "#A9B8BB"
EXTRA = """<style>
.dr{stroke-dasharray:var(--l);stroke-dashoffset:var(--l);animation:dr var(--d) linear both}
@keyframes dr{to{stroke-dashoffset:0}}
.fi{opacity:0;animation:fi .5s ease-out both} @keyframes fi{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}
</style>"""

def s_graph():
    dur = 12.0
    x0, x1, y0, y1 = 150, 960, 760, 1240   # grafik alanı
    phases = ["Yeleksiz", "Yelekli", "Yeleksiz", "Yelekli"]
    pw = (x1 - x0) / 4
    bands, labs = "", ""
    for i, p in enumerate(phases):
        xs = x0 + i * pw
        fill = MT if "Yelekli" == p else "#F3EDE2"
        bands += f'<rect x="{xs:.0f}" y="{y0}" width="{pw:.0f}" height="{y1-y0}" fill="{fill}" class="fi" style="animation-delay:{.4+i*.25:.2f}s"/>'
        if i: bands += f'<line x1="{xs:.0f}" y1="{y0}" x2="{xs:.0f}" y2="{y1}" stroke="#9AAEB1" stroke-width="3" stroke-dasharray="10 10" class="fi" style="animation-delay:{.4+i*.25:.2f}s"/>'
        labs += f'<text x="{xs+pw/2:.0f}" y="{y0-24}" text-anchor="middle" font-size="30" font-weight="900" fill="{A if p=="Yelekli" else "#5B6E72"}" class="fi" style="animation-delay:{.5+i*.25:.2f}s">{p}</text>'
    # temsilî veri: evreler arasında belirgin fark yok
    vals = [52, 60, 48, 57, 55, 50, 58, 53, 49, 56, 54, 51, 57, 52, 55, 50]
    n = len(vals); pts = []
    for i, v in enumerate(vals):
        x = x0 + (i + .5) * (x1 - x0) / n
        y = y1 - (v / 100) * (y1 - y0)
        pts.append((x, y))
    d = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    L = sum(((pts[i+1][0]-pts[i][0])**2 + (pts[i+1][1]-pts[i][1])**2) ** .5 for i in range(n-1))
    dots = "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="11" fill="{O}" class="fi" style="animation-delay:{1.6 + i*(4.0/n):.2f}s"/>' for i, (x, y) in enumerate(pts))
    svg = f'''<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0">
{bands}{labs}
<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{DK}" stroke-width="4"/>
<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{DK}" stroke-width="4"/>
<path d="{d}" fill="none" stroke="{O}" stroke-width="7" stroke-linejoin="round" class="dr" style="--l:{L:.0f};--d:4.0s;animation-delay:1.6s"/>
{dots}
<text x="{x0-20}" y="{(y0+y1)/2:.0f}" text-anchor="middle" font-size="26" font-weight="800" fill="#5B6E72" transform="rotate(-90 {x0-20} {(y0+y1)/2:.0f})">Yerinde oturma süresi</text>
</svg>'''
    head = f'<div class="wrap" style="top:300px;bottom:auto;display:block"><div class="ttl up" style="animation-delay:.05s">Nasıl test edildi?</div><div class="up" style="font-size:42px;line-height:1.25;font-weight:900;color:{DK};animation-delay:.25s">Aynı çocuk, yelekli ve yeleksiz dönemlerde gözlemlendi</div></div>'
    note = f'<div class="fi" style="position:absolute;left:96px;right:120px;top:1290px;font-size:36px;line-height:1.35;font-weight:800;color:{DK};animation-delay:6.2s">Çoğu çalışmada çizgi değişmedi: Yelek giyilince de giyilmeyince de davranış benzerdi.</div><div class="fi" style="position:absolute;left:96px;top:1440px;font-size:26px;font-weight:700;color:#7A8A8D;animation-delay:6.4s">Temsilî grafik</div>'
    return dur, EXTRA + head + svg + note

SCENES = [
    s_hook("Ağırlıklı yelek otizmli çocukları gerçekten sakinleştirir mi?"),
    s_graph(),
    s_stat("7", "çalışmayı inceleyen ilk derleme", "Sonuç: Ağırlıklı yelekler şu an için önerilemez."),
    s_points("Daha yeni bir derleme", ["Ağırlıklı yeleği kanıta dayalı bir uygulama olarak görmedi.",
                                       "Oturma, dikkat ve tekrarlayıcı davranışlarda tutarlı bir etki bulunmadı."]),
    s_not("Çocuğun duyusal ihtiyaçları önemsiz değil. Bazı çocuklar yeleği rahat bulabilir. Ama dikkat ve davranış sorununu çözmek için yeleğe güvenmek yerine nedene bakmak gerekiyor."),
    s_act("NE YAPABİLİRSİNİZ?", "Davranışın ne zaman ve neden olduğunu gözlemleyin. Hareket molası ve görsel destek gibi kanıta dayalı uygulamaları deneyin.",
          "Sizin sınıfınızda ya da evinizde ağırlıklı yelek kullanılıyor mu?", "Stephenson &amp; Carter (2009), <i>JADD</i> · Taylor ve ark. (2017), <i>RASD</i>"),
]

async def run():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": W, "height": H})
        await build("r8-yelek", SCENES, pg, "stills" in sys.argv)
        await b.close()
asyncio.run(run())
