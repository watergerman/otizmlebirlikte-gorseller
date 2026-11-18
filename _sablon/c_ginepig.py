"""20 Kasım carousel: ginepig deneyinin ayrıntıları (O'Haire ve ark., 2013)."""
import asyncio, os, shutil, sys
from playwright.async_api import async_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from hafta_1622 import EXTRA, BOOK
import overlap

REPO = os.path.dirname(D)
SLUG = "2026-11-20-c10-ginepig"
BASE_ORIG = BASE

slides = [
    cover("Bilim Ne Diyor?", "Ginepig deneyi: Ne oldu, ne olmadı?",
          "Dünkü Reels'te anlattığımız deneyin ayrıntıları: <i>PLoS ONE</i>'da yayımlanan bir sınıf çalışması."),
    cards_n("Deney", "Nasıl yapıldı?", [
        ("33 üçlü grup", "Her grupta bir otizmli çocuk ve iki sınıf arkadaşı vardı. Çocuklar 5–12 yaş arasındaydı."),
        ("İki ayrı oturum", "Gruplar 10'ar dakika önce oyuncaklarla, sonra iki ginepigle serbest oyun oynadı."),
        ("Video kaydı", "Oturumlar kaydedildi ve iki bağımsız gözlemci tarafından puanlandı.")]),
    cards_n("Bulgular", "Ginepigler ortamdayken", [
        ("Daha çok gülümseme", "Otizmli çocuklar daha sık gülümsedi ve güldü."),
        ("Daha çok sosyal yaklaşım", "Yetişkinlerle daha çok konuştular; arkadaşları da onlara daha sık yaklaştı."),
        ("Daha az sıkıntı", "Kaşlarını çatma, ağlama ve sızlanma azaldı.")]),
    stat("Şaşırtıcı ayrıntı", "%82", "otizmli çocuk ginepigleri tercih etti",
         "Ama arkadaşlarıyla konuşma oyuncaklı oturumlarda daha fazlaydı. Hayvan her şeyi değiştirmedi; ortamı yumuşattı.",
         "Küçük bir çalışma. İki hayvan, çeşitli oyuncaklarla karşılaştırıldı."),
    steps("Sınıfta ve evde", "Bunu nasıl kullanabilirsiniz?", [
        "Çocuğun ilgisini çeken bir canlı ya da nesneyi oyunun merkezine koyun.",
        "Arkadaşlarını da oyuna dahil edin; ortak ilgi, sohbeti kendiliğinden başlatır.",
        "Hayvanla etkileşim her zaman yetişkin gözetiminde ve çocuğun isteğine göre olsun."],
        "O'Haire, McKenzie, Beck &amp; Slaughter (2013), <i>PLoS ONE</i>, 8(2), e57010")[:-6]
        + f'<div class="save">{BOOK}Sonra dönmek için kaydet</div></div>',
]

async def main():
    import lib
    lib.BASE = BASE_ORIG + EXTRA
    out = f"{D}/_out_{SLUG}"
    if os.path.exists(out): shutil.rmtree(out)
    await lib.render({SLUG: slides}, out)
    probs = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for i in range(1, len(slides) + 1):
            await pg.goto(f"file://{out}/{SLUG}-{i}.html"); await pg.evaluate("document.fonts.ready")
            probs += await overlap.check(pg, f"{SLUG}-{i}")
        await b.close()
    if probs:
        print("\n".join(probs)); sys.exit("ÇAKIŞMA VAR")
    dst = f"{REPO}/{SLUG}"; os.makedirs(dst, exist_ok=True)
    for i in range(1, len(slides) + 1):
        shutil.copy(f"{out}/{SLUG}-{i}.jpg", f"{dst}/{i}.jpg")
    shutil.rmtree(out); print("ok", dst)

asyncio.run(main())
