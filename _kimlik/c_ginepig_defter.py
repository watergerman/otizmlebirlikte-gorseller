"""20 Kasım carousel — ginepig deneyinin ayrıntıları, araştırma defteri kimliğiyle."""
import os, sys, asyncio, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(f"{HERE}/sayfa_tipleri.py", encoding="utf-8").read().rsplit("asyncio.run(main())", 1)[0]
exec(src)

BOOK = (f'<div style="position:absolute;left:170px;bottom:150px;display:flex;align-items:center;gap:14px;font-weight:700;font-size:32px;color:{INK}">'
        f'<svg width="30" height="38" viewBox="0 0 30 38"><path d="M3 3h24v32l-12-9-12 9z" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/></svg>Sonra dönmek için kaydet</div>')

def p1():
    gp = (f'<g transform="translate(700 980) scale(1.3)" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
          f'<path d="M-62 6 C-64 -30 -20 -44 14 -40 C40 -60 78 -44 76 -14 C80 6 60 30 20 32 C-20 36 -60 34 -62 6 Z" fill="#E7B98A"/>'
          f'<path d="M30 -50 c4 -14 18 -14 18 -2" fill="#E7B98A"/><circle cx="54" cy="-18" r="4" fill="{INK}"/><path d="M-40 32 v12 M-10 34 v12 M30 30 v12"/></g>')
    body = (f'<svg width="1080" height="1350" style="position:absolute;left:0;top:0">{gp}'
            f'<path d="M470 905 C520 860 570 860 610 905" fill="none" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M598 884 l14 22 l-26 4" fill="none" stroke="{RED}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            f'<div class="w"><div class="no"><b>DENEY 07</b>AYRINTILAR</div><h1>Ginepig deneyi: <span class="hl">ne oldu,</span> ne olmadı?</h1>'
            f'<div class="p" style="margin-top:30px">Dünkü Reels\'te anlattığımız deneyin ayrıntıları.</div></div>'
            f'<div class="hand" style="position:absolute;left:170px;top:850px;font-size:46px;transform:rotate(-4deg)">kaydırın →</div>')
    return doc("bnd", body, "O'Haire ve ark. (2013), PLoS ONE", "1 / 5")

def p3():
    items = ["Daha çok gülümsediler", "Yetişkinlerle daha çok konuştular", "Arkadaşları onlara daha sık yaklaştı", "Kaşlarını çatma ve ağlama azaldı"]
    li = "".join(f'<div class="it"><div class="ck">{CK}</div><div>{t}</div></div>' for t in items)
    body = (f'<div class="w"><div class="no"><b>BULGU</b>GİNEPİGLER ORTAMDAYKEN</div><h2>Otizmli çocuklarda <span class="hl">ne değişti?</span></h2>{li}</div>'
            f'<div class="fig" style="left:170px;right:90px;top:930px;padding:26px 30px;transform:rotate(-.8deg)"><div class="tape" style="left:-24px;top:-22px"></div>'
            f'<div class="hand" style="font-size:42px">ama dikkat!</div><div class="p" style="font-size:31px;margin-top:4px">Arkadaşlarıyla konuşma oyuncaklı oturumlarda daha fazlaydı.</div></div>')
    return doc("bnd", body, "O'Haire ve ark. (2013), PLoS ONE", "3 / 5")

def p5():
    items = ["Çocuğun ilgisini çeken bir canlıyı ya da nesneyi oyunun merkezine koyun",
             "Arkadaşlarını da oyuna katın; ortak ilgi sohbeti kendiliğinden başlatır",
             "Hayvanla etkileşim her zaman yetişkin gözetiminde ve çocuğun isteğine göre olsun"]
    li = "".join(f'<div class="it"><div class="ck">{CK}</div><div>{t}</div></div>' for t in items)
    body = (f'<div class="w"><div class="no"><b>SINIFTA VE EVDE</b>NE YAPABİLİRSİNİZ?</div><h2>Oyunu çocuğun <span class="hl">ilgisi üzerine</span> kurun</h2>{li}'
            f'<div style="font-family:\'Mono\';font-size:22px;line-height:1.5;color:{MUTED};margin-top:44px">Kaynak: O\'Haire, McKenzie, Beck &amp; Slaughter (2013). PLoS ONE, 8(2), e57010.</div></div>{BOOK}')
    return doc("bnd", body, "Otizm Spektrum Bozukluğu Eğitimi Uzmanı", "5 / 5")

def p2():  # deney sayfası — sayfa_tipleri.deney ile aynı, sayfa numarası 2/5
    return deney()

def p4():
    h = rakam().replace("4 / 5", "4 / 5")
    return h

PAGES = {"1": p1, "2": p2, "3": p3, "4": p4, "5": p5}

async def main2():
    out = f"{HERE}/out/c_ginepig"; os.makedirs(out, exist_ok=True); probs = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for k, fn in PAGES.items():
            hp = f"{out}/{k}.html"; open(hp, "w", encoding="utf-8").write(fn())
            await pg.goto(f"file://{hp}"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(150)
            probs += await overlap.check(pg, k)
            await pg.screenshot(path=f"{out}/{k}.jpg", type="jpeg", quality=92)
        await b.close()
    if probs: print("\n".join(probs)); sys.exit("ÇAKIŞMA VAR")
    print("ok")
asyncio.run(main2())
