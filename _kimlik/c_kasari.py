import asyncio, sys
from defter_c import *
F = "Kasari ve ark. (2012), JCPP"
pages = [
 p_kartlar("bnd", "DENEY 08", "AYRINTILAR", 'Çocuklar kurayla <span class="hl">dört gruba</span> ayrıldı',
   ["Yalnızca otizmli çocuk eğitildi", "Yalnızca sınıf arkadaşları eğitildi", "İkisi birden eğitildi", "Olağan destek sürdü"],
   note="30 okul, 60 çocuk, 6 hafta", lead="Geçen cuma Reels'te anlattığımız çalışmanın ayrıntıları.", foot=F, page="1 / 5"),
 p_rakam("bnd", "SONUÇ", "KALICILIK", "Fark ne kadar sürdü?", "3 ay",
   note="3 ay sonra bile sürüyordu, ama yalnızca sınıf arkadaşlarının eğitildiği gruplarda", foot=F, page="2 / 5"),
 p_karsilastirma("bnd", "MİT Mİ?", "KARŞILAŞTIRMA", 'Önce <span class="hl">kimi</span> eğitmeli?',
   "Önce otizmli çocuğa sosyal beceri öğretmek gerekir.", "Fark, sınıf arkadaşları eğitilince ortaya çıktı.", foot=F, page="3 / 5"),
 p_kontrol("ogretmen", "LİSTE", "SINIFTA", 'Sınıfta <span class="hl">denemek</span> isterseniz',
   ["İki üç gönüllü öğrenci seçin", "Onlara arkadaşlarını oyuna nasıl çağıracaklarını gösterin", "Bir hafta boyunca teneffüste kimin kiminle oynadığını not alın"],
   foot="Öğretmen Köşesi", page="4 / 5"),
 p_soru("bnd", "Sınıfınızda gönüllü öğrencilerle böyle bir şey denediniz mi?",
   kunye="Kasari, Rotheram-Fuller, Locke ve Gulsrud (2012). Journal of Child Psychology and Psychiatry, 53(4).", foot="Otizm Spektrum Bozukluğu Eğitimi Uzmanı", page="5 / 5"),
]
probs = asyncio.run(render_set("kasari", pages, f"{HERE}/out/c_kasari"))
print("\n".join(probs) if probs else "ok")
