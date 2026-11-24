import asyncio
from defter_c import *
KOSE["gun"] = ("24 KASIM ÖĞRETMENLER GÜNÜ", "#3F7FBF", "#BFDCF7")
body = (f'<div class="w"><div class="no"><b>FARKINDALIK</b>2024–25 VERİLERİ</div>'
        f'<h2 style="font-size:66px">Öğretmenler Günü kutlu olsun</h2></div>'
        f'<div style="position:absolute;left:170px;right:90px;top:410px;font-weight:700;font-size:170px;letter-spacing:-5px;line-height:1"><span class="hl">602.729</span></div>'
        f'<div class="p" style="position:absolute;left:170px;right:90px;top:605px;font-size:36px">öğrenci geçen yıl okulda özel eğitim hizmeti aldı.</div>'
        f'<div class="hand" style="position:absolute;left:170px;right:90px;top:700px;font-size:50px;transform:rotate(-2deg)">ilkokul, ortaokul ve lisede her 4 öğrenciden 3\'ü genel sınıflarda okuyor</div>'
        f'<div class="fig" style="left:170px;right:90px;top:915px;padding:28px 32px;transform:rotate(-.8deg)"><div class="tape" style="left:-24px;top:-22px"></div>'
        f'<div style="font-weight:600;font-size:36px;line-height:1.32">Yani özel eğitim, yalnızca özel eğitim öğretmenlerinin işi değil. Bu öğrencilere sınıfının kapısını açan her öğretmenin günü kutlu olsun.</div></div>')
page = doc("gun", body, "Kaynak: MEB Örgün Eğitim İstatistikleri 2024–25", "")
probs = asyncio.run(render_set("ogretmen", [page], f"{HERE}/out/ogretmen"))
print("\n".join(probs) if probs else "ok")
