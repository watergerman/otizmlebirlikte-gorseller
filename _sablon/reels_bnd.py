"""Bilim Ne Diyor? Reels üretici. Kullanım: python3 reels_bnd.py [stills]"""
import asyncio, subprocess, os, sys, json
from playwright.async_api import async_playwright
from lib import font_css, D

W, H, FPS = 1080, 1920, 30
CSS = font_css + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
body{font-family:'Nunito',sans-serif;background:#FBF6EE;color:#23363A;position:relative}
.b1{position:absolute;width:900px;height:900px;border-radius:50%;background:#DDEFEA;top:-380px;right:-320px;animation:dr 5s ease-in-out both}
.b2{position:absolute;width:640px;height:640px;border-radius:50%;background:#FCE6D2;bottom:-260px;left:-240px;animation:dr2 5s ease-in-out both}
@keyframes dr{to{transform:translate(-40px,30px)}} @keyframes dr2{to{transform:translate(30px,-30px)}}
.wrap{position:absolute;left:96px;right:120px;top:330px;bottom:380px;display:flex;flex-direction:column;justify-content:center}
.up{opacity:0;animation:up .5s cubic-bezier(.2,.8,.2,1) both}
@keyframes up{from{opacity:0;transform:translateY(60px)}to{opacity:1;transform:none}}
.pop{opacity:0;animation:pop .45s cubic-bezier(.3,1.5,.5,1) both}
@keyframes pop{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:scale(1)}}
.tag{align-self:flex-start;background:#2F7F86;color:#fff;font-weight:900;font-size:40px;padding:16px 34px;border-radius:50px}
.hook{font-weight:900;font-size:104px;line-height:1.06;color:#1F5C62;margin-top:46px}
.big{font-weight:900;font-size:250px;line-height:1;color:#2F7F86}
.blab{font-weight:900;font-size:62px;line-height:1.2;color:#1F5C62;margin-top:26px}
.bsub{font-size:42px;line-height:1.35;color:#4E6266;margin-top:30px;font-weight:700}
.ttl{font-weight:900;font-size:50px;color:#F2994A;margin-bottom:34px}
.pt{background:#fff;border-radius:40px;padding:40px 48px;font-size:52px;line-height:1.28;font-weight:800;color:#23363A;margin-bottom:28px;box-shadow:0 10px 30px rgba(31,92,98,.08)}
.nm{background:#FDECEA;border-radius:44px;padding:52px 56px}
.nm span,.ac span{display:block;font-weight:900;font-size:38px;letter-spacing:2px;margin-bottom:16px}
.nm span{color:#C2483A}.nm p{font-size:54px;line-height:1.3;font-weight:800;color:#5A2A24}
.ac{background:#2F7F86;border-radius:44px;padding:52px 56px;color:#fff}
.ac span{color:#CFEDE8}.ac p{font-size:52px;line-height:1.3;font-weight:800}
.ask{margin-top:44px;font-size:52px;line-height:1.3;font-weight:900;color:#1F5C62}
.src{position:absolute;left:96px;right:120px;bottom:400px;font-size:30px;color:#6E7F82;font-weight:700}
.sig{position:absolute;left:96px;right:96px;top:150px;font-size:40px;font-weight:900;color:#2F7F86}
.sig small{display:block;font-size:30px;font-weight:700;color:#5B6E72;margin-top:6px}
.bar{position:absolute;left:96px;right:96px;top:100px;height:10px;border-radius:6px;background:#CFDCD9;overflow:hidden}
.bar i{display:block;height:100%;background:#2F7F86;transform-origin:left;animation:bar linear both}
@keyframes bar{from{transform:scaleX(var(--a))}to{transform:scaleX(var(--b))}}
"""

def frame(inner, k, n, dur):
    a, b = (k-1)/n, k/n
    return f'<div class="b1"></div><div class="b2"></div><div class="bar"><i style="--a:{a};--b:{b};animation-duration:{dur}s"></i></div><div class="sig">@otizmlebirlikte<small>Otizm Spektrum Bozukluğu Eğitimi Uzmanı</small></div>{inner}'

def s_hook(text): return 3.2, f'<div class="wrap"><div class="tag up" style="animation-delay:.05s">Bilim Ne Diyor?</div><div class="hook up" style="animation-delay:.2s">{text}</div></div>'
def s_stat(big, lab, sub): return 3.8, f'<div class="wrap"><div class="big pop" style="animation-delay:.1s">{big}</div><div class="blab up" style="animation-delay:.6s">{lab}</div><div class="bsub up" style="animation-delay:1.1s">{sub}</div></div>'
def s_points(t, pts):
    body = "".join(f'<div class="pt up" style="animation-delay:{.35+i*1.0:.2f}s">{p}</div>' for i,p in enumerate(pts))
    return 2.2 + 1.6*len(pts), f'<div class="wrap"><div class="ttl up" style="animation-delay:.05s">{t}</div>{body}</div>'
def s_not(text, lab="NE ANLAMA GELMİYOR?"): return 4.2, f'<div class="wrap"><div class="nm pop" style="animation-delay:.1s"><span>{lab}</span><p>{text}</p></div></div>'
def s_act(lab, text, ask, src): return 5.0, f'<div class="wrap"><div class="ac pop" style="animation-delay:.1s"><span>{lab}</span><p>{text}</p></div><div class="ask up" style="animation-delay:1.3s">{ask}</div></div><div class="src up" style="animation-delay:1.6s">Kaynak: {src}</div>'

REELS = {
 "r2-kardes": [
  s_hook("Otizmli bir çocuğun kardeşinde otizm görülme olasılığı ne kadar?"),
  s_stat("1/5", "Küçük kardeşlerde otizm tanısı (%20,2)", "1.605 bebeği izleyen çok merkezli bir çalışma"),
  s_points("Olasılığı artıranlar", ["Küçük kardeş erkekse %25,3 (kızsa %13,1)", "Birden fazla otizmli ağabey ya da abla varsa %36,9"]),
  s_not("Her kardeşte otizm görüleceği anlamına gelmez. Kardeşlerin yaklaşık 5'te 4'ünde görülmüyor."),
  s_act("NE YAPABİLİRSİNİZ?", "Küçük kardeşin gelişimini erken dönemden itibaren izleyin ve 18–24. aylarda tarama isteyin.", "Bu oranı tahmin edebilir miydiniz?", "Ozonoff ve ark. (2024), <i>Pediatrics</i>, 154(2)"),
 ],
 "r3-kizlar": [
  s_hook("Kızlarda otizm neden daha geç fark ediliyor?"),
  s_stat("3:1", "Erkek/kız oranı sanıldığı gibi 4:1 değil, 3:1'e daha yakın", "54 çalışmayı birleştiren meta-analiz"),
  s_points("Neden gözden kaçıyor?", ["Kızlar zorlandıkları davranışları gizleyebiliyor. Buna maskeleme deniyor.", "Göz temasını ve sohbeti taklit ederek “uyumlu” görünebiliyorlar."]),
  s_not("Her sessiz kız otizmli değildir. Ama “kızlarda otizm olmaz” düşüncesi tanıyı geciktirir."),
  s_act("NE YAPABİLİRSİNİZ?", "Okulda “sorunsuz” görünen bir kız evde sürekli tükenmiş görünüyorsa, bunu bir uzmanla konuşun.", "Çevrenizde geç tanı alan bir kız çocuğu var mı?", "Loomes ve ark. (2017), <i>JAACAP</i>, 56(6) · Hull ve ark. (2017), <i>JADD</i>, 47(8)"),
 ],
 "r4-cift-empati": [
  s_hook("Otizmli bireyler gerçekten “iletişim kuramıyor” mu?"),
  s_points("Deney", ["72 yetişkin, 8'er kişilik zincirler", "Bir hikâye kulaktan kulağa aktarıldı"]),
  s_points("Sonuç", ["Otizmli zincirler, otizmsiz zincirler kadar başarılıydı.", "En çok bilgi kaybı karma zincirlerde yaşandı."]),
  s_not("Otizmde iletişim güçlüğü olmadığını göstermez. Ama sorunun tek taraflı olmayabileceğini gösteriyor.", "NE ANLAMA GELİYOR?"),
  s_act("SINIFTA", "Otizmli öğrenciyi yalnızca “uyum sağlaması gereken” taraf olarak görmeyin. Karşılıklı anlamayı öğretin.", "Bu bulguyu bekliyor muydunuz?", "Crompton ve ark. (2020), <i>Autism</i>, 24(7)"),
 ],
 "r5-mikrobiyota": [
  s_hook("Bağırsak bakterileri otizme mi yol açıyor?"),
  s_stat("247", "çocuk incelendi", "99 otizmli çocuk, 51 kardeş ve 97 akran"),
  s_points("Bulgu", ["Otizmle bağırsak mikrobiyotası arasında doğrudan güçlü bir ilişki bulunmadı.", "Fark büyük ölçüde daha seçici ve az çeşitli beslenmeyle açıklanıyordu."]),
  s_not("Tek bir çalışma. Mikrobiyotanın hiçbir rolü olmadığını kanıtlamaz, ama “bağırsak otizme yol açar” iddiasını zayıflatıyor."),
  s_act("NE YAPABİLİRSİNİZ?", "Bağırsak temelli “tedavi” vaatlerine temkinli yaklaşın. Seçici yeme için bir uzmandan destek alın.", "Çocuğunuzda seçici yeme var mı?", "Yap ve ark. (2021), <i>Cell</i>, 184(24)"),
 ],
 "r6-goz-temasi": [
  s_hook("Otizmin izleri bebeklikte görülebilir mi?"),
  s_stat("2–6 ay", "Göze bakma bu dönemde azalmaya başladı", "Sonradan otizm tanısı alan bebeklerde, göz izleme çalışması"),
  s_points("Şaşırtıcı olan", ["Bu bebekler başta göze tipik düzeyde bakıyordu.", "Göze bakma zamanla azaldı. 24. ayda yaklaşık yarıya indi."]),
  s_not("Bunu gözle ayırt edemezsiniz, bu bir tanı aracı değil. Örneklem küçük ve bulgunun tekrarlanması gerekiyor."),
  s_act("NE ANLAMA GELİYOR?", "Erken dönem, gelişimin hâlâ şekillendiği bir pencere. Endişeniz varsa beklemeyin, değerlendirme isteyin.", "Bunu biliyor muydunuz?", "Jones &amp; Klin (2013), <i>Nature</i>, 504"),
 ],
}

async def build(slug, scenes, pg, stills):
    out = f"{D}/reels/{slug}"; os.makedirs(out, exist_ok=True)
    files = []
    for k, (dur, inner) in enumerate(scenes, 1):
        hp = f"{out}/s{k}.html"
        open(hp, "w", encoding="utf-8").write(f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{frame(inner, k, len(scenes), dur)}</body></html>")
        await pg.goto(f"file://{hp}")
        await pg.evaluate("document.fonts.ready")
        await pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        async def at(t): await pg.evaluate(f"document.getAnimations().forEach(a=>{{a.currentTime={t*1000}}})")
        if stills:
            await at(dur - 0.05); await pg.screenshot(path=f"{out}/s{k}-end.png"); continue
        tmp = f"{out}/s{k}.part.mp4"
        ff = subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-",
              "-vf","format=yuv420p","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p","-r",str(FPS),tmp], stdin=subprocess.PIPE)
        for i in range(int(round(dur*FPS))):
            await at(i/FPS); ff.stdin.write(await pg.screenshot(type="jpeg", quality=92))
        ff.stdin.close(); ff.wait(); assert ff.returncode == 0
        os.replace(tmp, f"{out}/s{k}.mp4"); files.append(f"{out}/s{k}.mp4")
    if stills: return
    open(f"{out}/list.txt","w").write("".join(f"file '{f}'\n" for f in files))
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{out}/list.txt","-c","copy",f"{out}/v.mp4"], check=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"{out}/v.mp4","-f","lavfi","-i","anullsrc=r=44100:cl=stereo",
                    "-c:v","copy","-c:a","aac","-shortest","-movflags","+faststart",f"{out}/reel.part.mp4"], check=True)
    os.replace(f"{out}/reel.part.mp4", f"{out}/reel.mp4")
    print(slug, sum(d for d,_ in scenes), "s")

async def main():
    stills = len(sys.argv) > 1
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width":W,"height":H})
        for slug, sc in REELS.items(): await build(slug, sc, pg, stills)
        await b.close()
asyncio.run(main())
