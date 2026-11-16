import asyncio, os
from playwright.async_api import async_playwright
from lib import font_css, D

OUT = f"{D}/layouts"; os.makedirs(OUT, exist_ok=True)
TEAL, DTEAL, ORG, CREAM, MINT, INK, RED = "#2F7F86", "#1F5C62", "#F2994A", "#FBF6EE", "#DDEFEA", "#23363A", "#C2483A"

CSS = font_css + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{font-family:'Nunito',sans-serif;background:{CREAM};color:{INK};position:relative}}
.tag{{display:inline-block;background:{TEAL};color:#fff;font-weight:900;font-size:28px;padding:12px 26px;border-radius:40px}}
.foot{{position:absolute;left:90px;right:90px;bottom:50px;font-size:27px;font-weight:900;color:{TEAL};line-height:1.25}}
.foot small{{display:block;font-size:22px;font-weight:700;color:#5B6E72}}
.src{{position:absolute;left:90px;right:90px;bottom:130px;font-size:22px;color:#7A8A8D;font-weight:700}}
"""

def person(color, x, y, s=1):
    return f'<g transform="translate({x} {y}) scale({s})"><circle cx="0" cy="-34" r="16" fill="{color}"/><path d="M-24 18 Q-24 -12 0 -12 Q24 -12 24 18 Z" fill="{color}"/></g>'

def chain(y, colors, loss_from=None, label="", note=""):
    g = ""
    for i, c in enumerate(colors):
        x = 120 + i * 112
        g += person(c, x, y)
        if i < len(colors) - 1:
            op = 1.0
            if loss_from is not None and i >= loss_from: op = max(.15, 1 - (i - loss_from + 1) * .22)
            g += f'<circle cx="{x+56}" cy="{y-40}" r="9" fill="{ORG}" opacity="{op}"/>'
    g += f'<text x="90" y="{y-90}" font-size="34" font-weight="900" fill="{DTEAL}">{label}</text>'
    g += f'<text x="990" y="{y-90}" font-size="30" font-weight="800" fill="{RED if loss_from is not None else TEAL}" text-anchor="end">{note}</text>'
    return g

def L1():
    A, N = TEAL, "#A9B8BB"
    svg = f'''<svg width="1080" height="760" viewBox="0 0 1080 760">
{chain(200, [A]*8, None, "Otizmli zincir", "Bilgi korunuyor")}
{chain(430, [N]*8, None, "Otizmsiz zincir", "Bilgi korunuyor")}
{chain(660, [A,N,A,N,A,N,A,N], 1, "Karma zincir", "En çok kayıp")}
</svg>'''
    return f'''<div style="position:absolute;inset:0;padding:90px 0 0">
<div style="padding:0 90px"><div class="tag">Bilim Ne Diyor? · Deney</div>
<div style="font-weight:900;font-size:66px;line-height:1.1;color:{DTEAL};margin-top:34px">Bir hikâye kulaktan kulağa aktarıldı</div>
<div style="font-size:32px;color:#4E6266;margin-top:18px;font-weight:700">72 yetişkin, 8'er kişilik zincirler. <span style="color:{ORG}">●</span> = aktarılan bilgi</div></div>
<div style="margin-top:20px">{svg}</div></div>
<div class="src">Crompton ve ark. (2020), <i>Autism</i>, 24(7)</div>
<div class="foot">@otizmlebirlikte<small>Otizm Spektrum Bozukluğu Eğitimi Uzmanı</small></div>'''

def L2():
    return f'''<div style="position:absolute;inset:0;background:{DTEAL}"></div>
<div style="position:absolute;width:760px;height:760px;border-radius:50%;background:{TEAL};opacity:.35;right:-260px;top:-200px"></div>
<div style="position:absolute;inset:0;padding:100px 90px;display:flex;flex-direction:column;justify-content:center;color:#fff">
<div class="tag" style="align-self:flex-start;background:{ORG}">Bilim Ne Diyor?</div>
<div style="font-weight:900;font-size:360px;line-height:1;margin-top:40px;letter-spacing:-8px">1/5</div>
<div style="font-weight:900;font-size:58px;line-height:1.2;margin-top:20px">Otizmli ağabey ya da ablası olan çocukların yaklaşık 5'te 1'i otizm tanısı alıyor.</div>
<div style="font-size:32px;line-height:1.4;margin-top:30px;color:#CFEDE8;font-weight:700">1.605 bebeği izleyen çok merkezli bir çalışma</div></div>
<div class="src" style="color:#9CC9C5">Ozonoff ve ark. (2024), <i>Pediatrics</i>, 154(2)</div>
<div class="foot" style="color:#fff">@otizmlebirlikte<small style="color:#9CC9C5">Otizm Spektrum Bozukluğu Eğitimi Uzmanı</small></div>'''

def L3():
    return f'''<div style="position:absolute;left:0;top:0;width:540px;height:1350px;background:#F3E3DF"></div>
<div style="position:absolute;left:540px;top:0;width:540px;height:1350px;background:{MINT}"></div>
<div style="position:absolute;left:0;right:0;top:90px;text-align:center"><div class="tag">Bilim Ne Diyor? · Kızlarda otizm</div></div>
<div style="position:absolute;left:0;width:540px;top:260px;text-align:center">
<div style="font-weight:900;font-size:40px;letter-spacing:2px;color:{RED}">SANILAN</div>
<div style="font-weight:900;font-size:220px;color:{RED};margin-top:30px;opacity:.85">4:1</div>
<div style="font-size:36px;font-weight:800;color:#5A2A24;padding:0 60px;line-height:1.3">Erkeklerde 4 kat daha sık</div></div>
<div style="position:absolute;left:540px;width:540px;top:260px;text-align:center">
<div style="font-weight:900;font-size:40px;letter-spacing:2px;color:{TEAL}">BULUNAN</div>
<div style="font-weight:900;font-size:220px;color:{DTEAL};margin-top:30px">3:1</div>
<div style="font-size:36px;font-weight:800;color:#1F4A4F;padding:0 60px;line-height:1.3">54 çalışmanın birleşik sonucu</div></div>
<div style="position:absolute;left:520px;top:520px;width:80px;height:80px;border-radius:50%;background:#fff;box-shadow:0 6px 20px rgba(0,0,0,.08);display:flex;align-items:center;justify-content:center;font-size:44px;color:{ORG};font-weight:900">→</div>
<div style="position:absolute;left:90px;right:90px;top:860px;background:#fff;border-radius:36px;padding:40px 46px;font-size:36px;line-height:1.4;font-weight:700;color:{INK};box-shadow:0 10px 30px rgba(31,92,98,.08)">Pek çok kız, zorlandığı davranışları gizleyebildiği için tanı almadan kalıyor olabilir.</div>
<div class="src">Loomes ve ark. (2017), <i>JAACAP</i>, 56(6)</div>
<div class="foot">@otizmlebirlikte<small>Otizm Spektrum Bozukluğu Eğitimi Uzmanı</small></div>'''

def L4():
    opt = lambda k, t: f'<div style="display:flex;align-items:center;gap:30px;background:#fff;border-radius:32px;padding:34px 40px;margin-bottom:26px;box-shadow:0 10px 30px rgba(31,92,98,.08)"><div style="flex:0 0 84px;height:84px;border-radius:50%;background:{ORG};color:#fff;font-weight:900;font-size:44px;display:flex;align-items:center;justify-content:center">{k}</div><div style="font-size:44px;font-weight:800;color:{INK}">{t}</div></div>'
    return f'''<div style="position:absolute;width:620px;height:620px;border-radius:50%;background:{MINT};top:-220px;right:-200px"></div>
<div style="position:absolute;inset:0;padding:100px 90px 220px;display:flex;flex-direction:column;justify-content:center">
<div class="tag" style="align-self:flex-start;background:{ORG}">Sence? 🤔</div>
<div style="font-weight:900;font-size:62px;line-height:1.12;color:{DTEAL};margin:36px 0 44px">Otizmli ve otizmsiz kişiler bir hikâyeyi kulaktan kulağa aktarsa, en çok bilgi hangi zincirde kaybolur?</div>
{opt("A","Otizmli zincirde")}{opt("B","Otizmsiz zincirde")}{opt("C","Karma zincirde")}
<div style="font-size:34px;font-weight:800;color:{TEAL};margin-top:20px">Cevabını yorumlara yaz, doğru cevap yarın 👇</div></div>
<div class="foot">@otizmlebirlikte<small>Otizm Spektrum Bozukluğu Eğitimi Uzmanı</small></div>'''

LAYOUTS = {"1-deney": L1, "2-tek-rakam": L2, "3-karsilastirma": L3, "4-sence": L4}

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for k, f in LAYOUTS.items():
            hp = f"{OUT}/{k}.html"
            open(hp, "w", encoding="utf-8").write(f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{f()}</body></html>")
            await pg.goto(f"file://{hp}"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(150)
            await pg.screenshot(path=f"{OUT}/{k}.png")
        await b.close()
asyncio.run(main())
