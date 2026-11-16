import asyncio, os, subprocess
from playwright.async_api import async_playwright
from lib import font_css, D
OUT = f"{D}/series"; os.makedirs(OUT, exist_ok=True)

SERIES = [  # ad, ana renk, koyu, açık zemin, örnek başlık, alt metin
 ("Bilim Ne Diyor?", "#2F7F86", "#1F5C62", "#DDEFEA", "Konuşmayan çocukların kaçı konuşmaya başlıyor?", "707 çocuğu kapsayan bir araştırmanın bulguları"),
 ("Günün İpucu", "#E07B39", "#A8501B", "#FCE6D2", "Övgünüz davranışı söylesin", "“Aferin” yerine “Oyuncaklarını toplaman harika!”"),
 ("Veli Köşesi", "#7A62B5", "#4F3D85", "#E9E3F6", "Öfke nöbeti anında ne yapmalı?", "Sırasında, sonrasında ve öncesinde atılacak adımlar"),
 ("Öğretmen Köşesi", "#3F7FBF", "#24568A", "#DFEAF6", "Sınıfınızda otizmli bir öğrenci mi var?", "Kaynaştırmada hemen uygulanabilecek 6 strateji"),
]

def card(name, c, dk, lt, title, sub):
    return f"""<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{font_css}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{font-family:'Nunito',sans-serif;background:#FBF6EE;position:relative}}
.b1{{position:absolute;width:620px;height:620px;border-radius:50%;background:{lt};top:-220px;right:-200px}}
.b2{{position:absolute;width:420px;height:420px;border-radius:50%;background:{lt};opacity:.6;bottom:-170px;left:-150px}}
.w{{position:absolute;inset:0;padding:96px 90px 160px;display:flex;flex-direction:column}}
.tag{{align-self:flex-start;background:{c};color:#fff;font-weight:900;font-size:30px;padding:14px 30px;border-radius:40px}}
h1{{font-weight:900;font-size:92px;line-height:1.06;color:{dk};margin-top:46px}}
p{{font-size:40px;line-height:1.4;font-weight:700;color:#3C5257;margin-top:36px}}
.sw{{margin-top:auto;font-size:34px;font-weight:800;color:{c}}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:22px;background:{c}}}
.f{{position:absolute;left:90px;bottom:50px;font-size:27px;font-weight:900;color:{c};line-height:1.25}} .f small{{display:block;font-size:22px;color:#5B6E72;font-weight:700}}
</style></head><body><div class="bar"></div><div class="b1"></div><div class="b2"></div>
<div class="w"><div class="tag">{name}</div><h1>{title}</h1><p>{sub}</p><div class="sw">Kaydır →</div></div>
<div class="f">@otizmlebirlikte<small>Otizm Spektrum Bozukluğu Eğitimi Uzmanı</small></div></body></html>"""

# --- hareketli şema: kulaktan kulağa zinciri (1080x1920, ~9 sn)
A, N, O, DK = "#2F7F86", "#A9B8BB", "#F2994A", "#1F5C62"
def anim_html():
    rows = [("Otizmli zincir", [A]*6, None, .6), ("Otizmsiz zincir", [N]*6, None, 3.2), ("Karma zincir", [A,N,A,N,A,N], 1, 5.8)]
    g, css = "", ""
    for r, (lab, cols, loss, t0) in enumerate(rows):
        y = 640 + r * 380
        g += f'<text x="96" y="{y-120}" font-size="44" font-weight="900" fill="{DK}" class="fi" style="animation-delay:{t0-.4}s">{lab}</text>'
        for i, c in enumerate(cols):
            x = 150 + i * 156
            g += f'<g class="pop" style="animation-delay:{t0-.4+i*.05:.2f}s;transform-origin:{x}px {y}px"><circle cx="{x}" cy="{y-46}" r="22" fill="{c}"/><path d="M{x-33} {y+26} Q{x-33} {y-16} {x} {y-16} Q{x+33} {y-16} {x+33} {y+26} Z" fill="{c}"/></g>'
        # gezinen nokta: her adımda bir sonraki kişiye gider
        steps = len(cols) - 1; dur = 2.2
        kf = ""
        for s in range(steps + 1):
            pct = s / steps * 100
            op = 1.0 if (loss is None or s <= loss) else max(.12, 1 - (s - loss) * .24)
            sc = 1.0 if (loss is None or s <= loss) else max(.45, 1 - (s - loss) * .14)
            kf += f"{pct:.1f}%{{transform:translate({s*156}px,0) scale({sc});opacity:{op}}}"
        css += f"@keyframes m{r}{{{kf}}}"
        g += f'<g class="fi" style="animation-delay:{t0-.2:.2f}s"><circle cx="150" cy="{y-110}" r="20" fill="{O}" style="transform-box:fill-box;transform-origin:center;animation:m{r} {dur}s linear {t0}s both"/></g>'
        res = "Bilgi korunuyor" if loss is None else "En çok bilgi kaybı"
        colr = A if loss is None else "#C2483A"
        g += f'<text x="984" y="{y+110}" font-size="40" font-weight="900" fill="{colr}" text-anchor="end" class="fi" style="animation-delay:{t0+dur:.1f}s">{res}</text>'
    return f"""<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{font_css}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:1080px;height:1920px;overflow:hidden}}
body{{font-family:'Nunito',sans-serif;background:#FBF6EE}}
.fi{{opacity:0;animation:fi .45s ease-out both}} @keyframes fi{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:none}}}}
.pop{{opacity:0;animation:pp .4s cubic-bezier(.3,1.5,.5,1) both}} @keyframes pp{{from{{opacity:0;transform:scale(.4)}}to{{opacity:1;transform:scale(1)}}}}
{css}
.t{{position:absolute;left:96px;right:120px;top:170px}}
.tag{{display:inline-block;background:{A};color:#fff;font-weight:900;font-size:38px;padding:14px 32px;border-radius:50px}}
h1{{font-weight:900;font-size:70px;line-height:1.1;color:{DK};margin-top:28px}}
</style></head><body>
<div class="t"><div class="tag">Bilim Ne Diyor? · Deney</div><h1>Bir hikâye kulaktan kulağa aktarıldı</h1></div>
<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0">{g}</svg>
</body></html>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for i, s in enumerate(SERIES, 1):
            hp = f"{OUT}/s{i}.html"; open(hp, "w", encoding="utf-8").write(card(*s))
            await pg.goto(f"file://{hp}"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(150)
            await pg.screenshot(path=f"{OUT}/s{i}.png")
        pg2 = await b.new_page(viewport={"width":1080,"height":1920})
        hp = f"{OUT}/anim.html"; open(hp, "w", encoding="utf-8").write(anim_html())
        await pg2.goto(f"file://{hp}"); await pg2.evaluate("document.fonts.ready")
        await pg2.evaluate("document.getAnimations().forEach(a=>a.pause())")
        FPS, DUR = 30, 10.0
        tmp = f"{OUT}/anim.part.mp4"
        ff = subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-",
              "-vf","format=yuv420p","-c:v","libx264","-crf","20","-preset","veryfast","-pix_fmt","yuv420p","-movflags","+faststart",tmp], stdin=subprocess.PIPE)
        for i in range(int(DUR*FPS)):
            await pg2.evaluate(f"document.getAnimations().forEach(a=>{{a.currentTime={i/FPS*1000}}})")
            ff.stdin.write(await pg2.screenshot(type="jpeg", quality=90))
        ff.stdin.close(); ff.wait(); os.replace(tmp, f"{OUT}/hareketli-sema-ornek.mp4")
        await b.close()
asyncio.run(main())
