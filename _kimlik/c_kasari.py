import asyncio, sys
from defter_c import *
F = "Kasari ve ark. (2012), JCPP"
kids = "".join(f'<g transform="translate({x} {y})" stroke="{INK}" stroke-width="4"><circle cx="0" cy="-60" r="22" fill="{c}"/><path d="M-32 0 Q-32 -34 0 -34 Q32 -34 32 0 Z" fill="{c}"/></g>'
               for x, y, c in [(300, 1010, "#C9D3E0"), (400, 960, "#C9D3E0"), (500, 1020, "#C9D3E0"), (400, 1080, "#C9D3E0"), (820, 990, "#E7B98A")])
kapak = doc("bnd", (f'<svg width="1080" height="1350" style="position:absolute;left:0;top:0">{kids}'
    f'<circle cx="820" cy="930" r="52" fill="none" stroke="{RED}" stroke-width="5" stroke-dasharray="9 9"/></svg>'
    f'<div class="w"><div class="no"><b>DENEY 08</b>BİLİM NE DİYOR?</div>'
    f'<h1 style="font-size:84px">Otizmli çocuğun sınıfta arkadaş edinmesi için <span class="hl">kimi eğitmeli?</span></h1></div>'
    f'<div class="hand" style="position:absolute;left:640px;top:1090px;font-size:44px;transform:rotate(-3deg)">çocuğu mu?</div>'
    f'<div class="hand" style="position:absolute;left:200px;top:1120px;font-size:44px;transform:rotate(-2deg)">arkadaşlarını mı?</div>'), F, "1 / 6")
pages = [
 kapak,
 p_kartlar("bnd", "DENEY", "NASIL YAPILDI?", 'Bunu anlamak için 60 çocuk <span class="hl">dört gruba</span> ayrıldı',
   ["Yalnızca otizmli çocuk eğitildi", "Yalnızca sınıf arkadaşları eğitildi", "İkisi birden eğitildi", "Olağan destek sürdü"],
   note="30 okul, 1.–5. sınıflar, 6 hafta", foot=F, page="2 / 6"),
 p_kartlar("bnd", "ÖLÇÜM", "NEYE BAKTILAR?", 'Arkadaşlığı <span class="hl">nasıl ölçtüler?</span>',
   ["Sınıfa sordular: Kim kiminle takılıyor?", "Çocuklara sordular: En yakın arkadaşların kim?", "Öğretmen sosyal becerilerini değerlendirdi", "Teneffüste her hafta gözlem yapıldı"],
   foot=F, page="3 / 6"),
 p_kontrol("bnd", "SONUÇ", "NE BULDULAR?", 'Sınıf arkadaşları <span class="hl">eğitilince</span> otizmli çocuklar',
   ["Sınıftaki arkadaş gruplarına daha çok girdi", "Daha fazla sınıf arkadaşı onları “arkadaşım” diye gösterdi", "Öğretmenler sosyal becerilerini daha iyi buldu", "Teneffüste daha az yalnız kaldı"],
   note_title="3 ay sonra da sürüyordu", note="Otizmli çocuğun tek başına eğitildiği grupta ise bu değişiklikler görülmedi.", foot=F, page="4 / 6"),
 p_kontrol("ogretmen", "LİSTE", "SINIFTA", 'Sınıfta <span class="hl">denemek</span> isterseniz',
   ["İki üç gönüllü öğrenci seçin", "Onlara arkadaşlarını oyuna nasıl çağıracaklarını gösterin", "Bir hafta boyunca teneffüste kimin kiminle oynadığını not alın"],
   foot="Öğretmen Köşesi", page="5 / 6"),
 p_soru("bnd", "Sınıfınızda gönüllü öğrencilerle böyle bir şey denediniz mi?",
   kunye="Kasari, Rotheram-Fuller, Locke ve Gulsrud (2012). Journal of Child Psychology and Psychiatry, 53(4).", foot="Otizm Spektrum Bozukluğu Eğitimi Uzmanı", page="6 / 6"),
]
probs = asyncio.run(render_set("kasari", pages, f"{HERE}/out/c_kasari"))
print("\n".join(probs) if probs else "ok")
