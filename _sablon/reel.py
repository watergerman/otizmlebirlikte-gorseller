import asyncio, subprocess, os, sys
from playwright.async_api import async_playwright
from lib import font_css, D

OUT = f"{D}/reel"; os.makedirs(OUT, exist_ok=True)
W, H, FPS = 1080, 1920, 30

CSS = font_css + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
body{font-family:'Nunito',sans-serif;background:#FBF6EE;color:#23363A;position:relative}
.b1{position:absolute;width:900px;height:900px;border-radius:50%;background:#DDEFEA;top:-380px;right:-320px;animation:drift 4s ease-in-out both}
.b2{position:absolute;width:640px;height:640px;border-radius:50%;background:#FCE6D2;bottom:-260px;left:-240px;animation:drift2 4s ease-in-out both}
@keyframes drift{from{transform:translate(0,0)}to{transform:translate(-40px,30px)}}
@keyframes drift2{from{transform:translate(0,0)}to{transform:translate(30px,-30px)}}
.wrap{position:absolute;inset:0;padding:0 96px;display:flex;flex-direction:column;justify-content:center}
.up{opacity:0;animation:up .5s cubic-bezier(.2,.8,.2,1) both}
@keyframes up{from{opacity:0;transform:translateY(60px)}to{opacity:1;transform:none}}
.pop{opacity:0;animation:pop .45s cubic-bezier(.3,1.6,.5,1) both}
@keyframes pop{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:scale(1)}}
.strike{text-decoration:line-through;text-decoration-thickness:9px;text-decoration-color:rgba(194,72,58,0);animation:st .35s ease-out both}
@keyframes st{to{text-decoration-color:rgba(194,72,58,1)}}
.tag{align-self:flex-start;background:#2F7F86;color:#fff;font-weight:900;font-size:40px;padding:16px 34px;border-radius:50px}
.hook{font-weight:900;font-size:118px;line-height:1.05;color:#1F5C62;margin-top:50px}
.hook em{font-style:normal;color:#F2994A}
.n{font-weight:900;font-size:56px;color:#F2994A;margin-bottom:22px}
.quote{background:#FDECEA;border-radius:44px;padding:56px 60px;font-weight:900;font-size:84px;line-height:1.12;color:#5A2A24}
.fact{margin-top:44px;background:#E3F2EE;border-radius:44px;padding:48px 56px;font-size:54px;line-height:1.3;color:#1F4A4F;font-weight:700}
.fact span{display:block;font-weight:900;font-size:36px;letter-spacing:2px;color:#2F7F86;margin-bottom:12px}
.cta1{font-weight:900;font-size:62px;color:#3C5257;margin-bottom:20px}
.cta2{background:#2F7F86;color:#fff;border-radius:44px;padding:56px 60px;font-weight:900;font-size:96px;line-height:1.1}
.ask{margin-top:70px;font-size:56px;line-height:1.3;font-weight:800;color:#1F5C62}
.sig{position:absolute;left:96px;right:96px;top:160px;font-size:40px;font-weight:900;color:#2F7F86}
.sig small{display:block;font-size:30px;font-weight:700;color:#5B6E72;margin-top:6px}
.bar{position:absolute;left:96px;right:96px;top:110px;height:10px;border-radius:6px;background:#CFDCD9;overflow:hidden}
.bar i{display:block;height:100%;background:#2F7F86;transform-origin:left;transform:scaleX(var(--s))}
"""

def sig(): return '<div class="sig">@otizmlebirlikte<small>Otizm Spektrum Bozukluğu Eğitimi Uzmanı</small></div>'
def bar(k): return f'<div class="bar"><i style="--s:{k/3}"></i></div>'

def item(k, q, f):
    return f"""<div class="b1"></div><div class="b2"></div>{bar(k)}<div class="wrap">
<div class="n up" style="animation-delay:.05s">{k} / 3</div>
<div class="quote pop" style="animation-delay:.15s"><span class="strike" style="animation-delay:1.1s">{q}</span></div>
<div class="fact up" style="animation-delay:1.35s"><span>GERÇEK</span>{f}</div>
</div>{sig()}"""

SCENES = [
 ("s1", 3.0, f"""<div class="b1"></div><div class="b2"></div><div class="wrap">
<div class="tag up" style="animation-delay:.05s">Veliler ve öğretmenler</div>
<div class="hook up" style="animation-delay:.25s">Otizmli bir çocuğun velisine bu <em>3 cümleyi</em> söylemeyin</div>
</div>{sig()}"""),
 ("s2", 3.6, item(1, "“Büyüyünce geçer.”", "Otizm yaşam boyu süren bir farklılıktır. Beklemek yerine erken destek fark yaratır.")),
 ("s3", 3.6, item(2, "“Biraz disiplin lazım.”", "Otizm terbiye eksikliği değil, nörogelişimsel bir farklılıktır.")),
 ("s4", 3.6, item(3, "“Hiç otizmli gibi görünmüyor.”", "Otizmin tek bir “görünüşü” yoktur. Her çocuk farklıdır.")),
 ("s5", 4.2, f"""<div class="b1"></div><div class="b2"></div><div class="wrap">
<div class="cta1 up" style="animation-delay:.05s">Bunun yerine şunu sorun:</div>
<div class="cta2 pop" style="animation-delay:.3s">“Nasıl destek olabilirim?”</div>
<div class="ask up" style="animation-delay:1.0s">Siz en çok hangisini duydunuz?<br>Yoruma yazın.</div>
</div>{sig()}"""),
]

async def main(only_stills=False):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": W, "height": H})
        files = []
        for name, dur, body in SCENES:
            hp = f"{OUT}/{name}.html"
            open(hp, "w", encoding="utf-8").write(f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
            await pg.goto(f"file://{hp}")
            await pg.evaluate("document.fonts.ready")
            await pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
            async def at(t):
                await pg.evaluate(f"document.getAnimations().forEach(a=>{{a.currentTime={t*1000}}})")
            if only_stills:
                await at(dur - 0.1); await pg.screenshot(path=f"{OUT}/{name}-end.png"); continue
            tmp = f"{OUT}/{name}.part.mp4"
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                                   "-vf", "format=yuv420p", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS), tmp],
                                  stdin=subprocess.PIPE)
            n = int(round(dur * FPS))
            for i in range(n):
                await at(i / FPS)
                ff.stdin.write(await pg.screenshot(type="jpeg", quality=92))
            ff.stdin.close(); ff.wait()
            assert ff.returncode == 0
            os.replace(tmp, f"{OUT}/{name}.mp4"); files.append(f"{OUT}/{name}.mp4")
        await b.close()
    if only_stills: return
    open(f"{OUT}/list.txt", "w").write("".join(f"file '{f}'\n" for f in files))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/list.txt", "-c", "copy", f"{OUT}/video.mp4"], check=True)
    # silent stereo track (Instagram expects audio)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{OUT}/video.mp4", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
                    "-c:v", "copy", "-c:a", "aac", "-shortest", "-movflags", "+faststart", f"{OUT}/reel.part.mp4"], check=True)
    os.replace(f"{OUT}/reel.part.mp4", f"{OUT}/reel.mp4")
    print("ok")

asyncio.run(main(only_stills=len(sys.argv) > 1))
