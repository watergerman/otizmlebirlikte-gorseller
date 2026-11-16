"""18 Kasım: ağırlıklı yelek carousel (Bilim Ne Diyor? petrol) + 2 hikâye. Çakışma denetimi dahil."""
import asyncio, os
from playwright.async_api import async_playwright
from lib import font_css, D
from overlap import check
OUT = f"{D}/yelek"; os.makedirs(OUT, exist_ok=True)
C, DK, LT, O, CR, INK, RED = "#2F7F86", "#1F5C62", "#DDEFEA", "#F2994A", "#FBF6EE", "#23363A", "#C2483A"

BASE = font_css + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Nunito',sans-serif;background:{CR};color:{INK};position:relative;overflow:hidden}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:22px;background:{C}}}
.b1{{position:absolute;width:620px;height:620px;border-radius:50%;background:{LT};top:-220px;right:-200px}}
.tag{{display:inline-block;background:{C};color:#fff;font-weight:900;font-size:30px;padding:14px 30px;border-radius:40px}}
.foot{{position:absolute;left:90px;bottom:50px;font-size:27px;font-weight:900;color:{C};line-height:1.25}}
.foot small{{display:block;font-size:22px;color:#5B6E72;font-weight:700}}
.dots{{position:absolute;right:90px;bottom:62px;display:flex;gap:10px}}.dots i{{width:14px;height:14px;border-radius:50%;background:#CFDCD9}}.dots i.on{{background:{C};width:38px;border-radius:8px}}
.card{{background:#fff;border-radius:34px;padding:36px 42px;box-shadow:0 10px 30px rgba(31,92,98,.08);margin-bottom:24px}}
.card h3{{font-size:40px;font-weight:900;color:{DK};margin-bottom:8px}} .card p{{font-size:33px;line-height:1.4;color:#3C5257}}
"""
def foot(n, t):
    d = "" if t == 1 else '<div class="dots">' + "".join(f'<i class="{"on" if i==n else ""}"></i>' for i in range(1, t+1)) + "</div>"
    return f'<div class="foot">@otizmlebirlikte<small>Otizm Spektrum Bozukluğu Eğitimi Uzmanı</small></div>{d}'

S = []
S.append(f'''<div class="bar"></div><div class="b1"></div>
<div style="position:absolute;inset:0;padding:96px 90px 170px;display:flex;flex-direction:column">
<div class="tag" style="align-self:flex-start">Bilim Ne Diyor?</div>
<div style="font-weight:900;font-size:92px;line-height:1.06;color:{DK};margin-top:46px">Ağırlıklı yelek gerçekten işe yarıyor mu?</div>
<div style="font-size:40px;line-height:1.4;font-weight:700;color:#3C5257;margin-top:36px">Sınıflarda ve evlerde sık kullanılan bir yöntemi araştırmalarla karşılaştırdık.</div>
<div style="margin-top:auto;font-size:34px;font-weight:800;color:{C}">Kaydır →</div></div>''')
# karşılaştırma düzeni
S.append(f'''<div style="position:absolute;left:0;top:0;width:540px;height:1350px;background:#F3E3DF"></div>
<div style="position:absolute;left:540px;top:0;width:540px;height:1350px;background:{LT}"></div>
<div style="position:absolute;left:0;right:0;top:90px;text-align:center"><div class="tag">Sanılan / Bulunan</div></div>
<div style="position:absolute;left:0;width:540px;top:250px;padding:0 56px;text-align:center">
<div style="font-weight:900;font-size:40px;letter-spacing:2px;color:{RED}">SANILAN</div>
<div style="font-size:44px;line-height:1.3;font-weight:900;color:#5A2A24;margin-top:40px">Yelek çocuğu sakinleştirir, dikkatini artırır, yerinde daha uzun oturmasını sağlar.</div></div>
<div style="position:absolute;left:540px;width:540px;top:250px;padding:0 56px;text-align:center">
<div style="font-weight:900;font-size:40px;letter-spacing:2px;color:{C}">BULUNAN</div>
<div style="font-size:44px;line-height:1.3;font-weight:900;color:{DK};margin-top:40px">Çoğu çalışmada oturma, dikkat ve tekrarlayıcı davranışlarda tutarlı bir fark bulunmadı.</div></div>
<div style="position:absolute;left:90px;right:90px;top:900px;background:#fff;border-radius:34px;padding:36px 42px;font-size:34px;line-height:1.4;font-weight:700;box-shadow:0 10px 30px rgba(31,92,98,.08)">Araştırmalarda aynı çocuk yelekli ve yeleksiz dönemlerde gözlemlenip karşılaştırıldı.</div>''')
# tek rakam düzeni (koyu zemin)
S.append(f'''<div style="position:absolute;inset:0;background:{DK}"></div>
<div style="position:absolute;width:760px;height:760px;border-radius:50%;background:{C};opacity:.35;right:-260px;top:-200px"></div>
<div style="position:absolute;inset:0;padding:100px 90px 200px;display:flex;flex-direction:column;justify-content:center;color:#fff">
<div class="tag" style="align-self:flex-start;background:{O}">İlk derleme</div>
<div style="font-weight:900;font-size:340px;line-height:1;margin-top:30px">7</div>
<div style="font-weight:900;font-size:56px;line-height:1.2;margin-top:10px">çalışma incelendi.</div>
<div style="font-size:40px;line-height:1.4;margin-top:30px;color:#CFEDE8;font-weight:800">Sonuç: Ağırlıklı yelekler şu an için önerilemez.</div>
<div style="font-size:26px;margin-top:36px;color:#9CC9C5;font-weight:700">Stephenson &amp; Carter (2009), <i>JADD</i>, 39(1)</div></div>''')
S.append(f'''<div class="bar"></div><div class="b1"></div>
<div style="position:absolute;inset:0;padding:110px 90px 170px;display:flex;flex-direction:column;justify-content:center">
<div style="font-weight:900;font-size:68px;line-height:1.1;color:{DK};margin-bottom:40px">Daha yeni bir derleme ne dedi?</div>
<div class="card"><h3>Kanıta dayalı değil</h3><p>Ağırlıklı yelek, otizmde kanıta dayalı bir uygulama olarak görülmedi.</p></div>
<div style="background:#FDECEA;border-radius:34px;padding:36px 42px"><div style="font-weight:900;font-size:30px;letter-spacing:2px;color:{RED};margin-bottom:12px">NE ANLAMA GELMİYOR?</div>
<p style="font-size:34px;line-height:1.4;font-weight:800;color:#5A2A24">Çocuğun duyusal ihtiyaçları önemsiz değil. Bazı çocuklar yeleği rahat bulabilir. Ama sorunu çözmek için yeleğe güvenmek yerine nedene bakmak gerekir.</p></div>
<div style="font-size:26px;margin-top:30px;color:#7A8A8D;font-weight:700">Taylor ve ark. (2017), <i>Research in Autism Spectrum Disorders</i></div></div>''')
li = lambda k, t: f'<div style="display:flex;gap:24px;align-items:flex-start;margin-bottom:30px;font-size:36px;line-height:1.4;color:#3C5257"><div style="flex:0 0 58px;height:58px;border-radius:50%;background:{C};color:#fff;font-weight:900;font-size:30px;display:flex;align-items:center;justify-content:center">{k}</div><div>{t}</div></div>'
S.append(f'''<div class="bar"></div><div class="b1"></div>
<div style="position:absolute;inset:0;padding:110px 90px 170px;display:flex;flex-direction:column">
<div class="tag" style="align-self:flex-start">Bunun yerine</div>
<div style="font-weight:900;font-size:68px;line-height:1.1;color:{DK};margin:36px 0 40px">Ne yapabilirsiniz?</div>
{li(1,"<b>Gözlemleyin:</b> Davranış ne zaman, hangi ortamda ve neyin ardından oluyor?")}
{li(2,"<b>Kanıta dayalı uygulamaları deneyin:</b> Hareket molası, görsel destek, öncül düzenlemeler.")}
{li(3,"<b>Bir uzmanla konuşun:</b> Duyusal hassasiyet varsa birlikte değerlendirin.")}
<div style="margin-top:auto;font-size:30px;font-weight:800;color:{C}">🔖 Sonra dönmek için kaydet</div>
<div style="font-size:24px;margin-top:16px;color:#7A8A8D;font-weight:700">Kaynaklar: Stephenson &amp; Carter (2009), <i>JADD</i>, 39(1), 105–114 · Taylor ve ark. (2017), <i>RASD</i> · Steinbrenner ve ark. (2020), NCAEP</div></div>''')

def story(inner):
    return f'''<div class="b1"></div><div style="position:absolute;inset:0;padding:300px 96px 420px;display:flex;flex-direction:column;justify-content:center">{inner}</div>
<div style="position:absolute;left:96px;top:150px;font-size:36px;font-weight:900;color:{C}">@otizmlebirlikte</div>'''
opt = lambda k, t: f'<div style="display:flex;align-items:center;gap:28px;background:#fff;border-radius:32px;padding:32px 38px;margin-bottom:24px;box-shadow:0 10px 30px rgba(31,92,98,.08)"><div style="flex:0 0 80px;height:80px;border-radius:50%;background:{O};color:#fff;font-weight:900;font-size:42px;display:flex;align-items:center;justify-content:center">{k}</div><div style="font-size:42px;font-weight:800;color:{INK};line-height:1.25">{t}</div></div>'
ST = {
 "hikaye-sence": story(f'''<div class="tag" style="align-self:flex-start;background:{O}">Sence? 🤔</div>
<div style="font-weight:900;font-size:66px;line-height:1.12;color:{DK};margin:40px 0 46px">Ağırlıklı yelek otizmli çocukların dikkatini ve yerinde oturmasını artırıyor mu?</div>
{opt("A","Evet, kanıtlandı")}{opt("B","Araştırmalar desteklemiyor")}{opt("C","Henüz hiç araştırılmadı")}
<div style="font-size:38px;font-weight:900;color:{C};margin-top:24px">Cevap bugün 17:30'da Reels'te 👀</div>'''),
 "hikaye-duyuru": story(f'''<div class="tag" style="align-self:flex-start">Yeni Reels · Bilim Ne Diyor?</div>
<div style="font-weight:900;font-size:84px;line-height:1.08;color:{DK};margin-top:44px">Ağırlıklı yelek gerçekten işe yarıyor mu?</div>
<div style="font-size:44px;line-height:1.35;font-weight:800;color:#3C5257;margin-top:40px">Sabahki sorunun cevabı burada. Doğru tahmin ettiniz mi?</div>
<div style="font-size:42px;font-weight:900;color:{O};margin-top:50px">Profilde izleyin →</div>'''),
}

async def main():
    issues = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for i, body in enumerate(S, 1):
            ft = foot(i, len(S))
            if i == 3: ft = ft.replace('class="foot"', 'class="foot" style="color:#fff"').replace("<small>", '<small style="color:#9CC9C5">')
            html = f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{BASE}html,body{{width:1080px;height:1350px}}</style></head><body>{body}{ft}</body></html>"
            hp = f"{OUT}/c{i}.html"; open(hp, "w", encoding="utf-8").write(html)
            await pg.goto(f"file://{hp}"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(150)
            issues += await check(pg, f"carousel {i}")
            await pg.screenshot(path=f"{OUT}/{i}.jpg", type="jpeg", quality=90)
        pg2 = await b.new_page(viewport={"width":1080,"height":1920})
        for k, body in ST.items():
            html = f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{BASE}html,body{{width:1080px;height:1920px}}</style></head><body>{body}</body></html>"
            hp = f"{OUT}/{k}.html"; open(hp, "w", encoding="utf-8").write(html)
            await pg2.goto(f"file://{hp}"); await pg2.evaluate("document.fonts.ready"); await pg2.wait_for_timeout(150)
            issues += await check(pg2, k)
            await pg2.screenshot(path=f"{OUT}/{k}.jpg", type="jpeg", quality=90)
        await b.close()
    print("ÇAKIŞMA SAYISI:", len(issues))
asyncio.run(main())
