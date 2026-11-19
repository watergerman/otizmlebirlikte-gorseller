"""Araştırma defteri kimliği: 5 sayfa tipi örneği (1080x1350)."""
import asyncio, os, sys
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/claude/otizmlebirlikte-gorseller/_sablon")
import overlap
F = f"file://{HERE}/node_modules/@fontsource"
RNG = {"latin": "U+0000-00FF,U+2000-206F,U+20AC,U+2122", "latin-ext": "U+0100-024F,U+1E00-1EFF,U+2190-21FF"}
def ff(fam, pkg, weights):
    return "".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('{F}/{pkg}/files/{pkg}-{s}-{w}-normal.woff2');unicode-range:{RNG[s]}}}" for w in weights for s in RNG)
FONTS = ff("Sans", "instrument-sans", (400, 500, 600, 700)) + ff("Mono", "geist-mono", (400, 500)) + ff("Hand", "kalam", (400, 700))
INK, RED, MUTED = "#1E2A44", "#D2553F", "#7C6F55"
KOSE = {  # ad, sekme rengi, vurgu rengi
    "bnd": ("BİLİM NE DİYOR?", "#1E2A44", "#FFE16A"),
    "ipucu": ("GÜNÜN İPUCU", "#E07B39", "#FFD0A3"),
    "veli": ("VELİ KÖŞESİ", "#7A62B5", "#D9CCF7"),
    "ogretmen": ("ÖĞRETMEN KÖŞESİ", "#3F7FBF", "#BFDCF7"),
}
def css(hl):
    return f"""{FONTS}*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{background:#F6F1E6;font-family:'Sans';color:{INK};position:relative}}
body:before{{content:"";position:absolute;inset:0;background-image:linear-gradient(#E4DCC8 1.5px,transparent 1.5px),linear-gradient(90deg,#E4DCC8 1.5px,transparent 1.5px);background-size:54px 54px;opacity:.75}}
.margin{{position:absolute;top:0;bottom:0;left:118px;width:3px;background:#E39B95}}
.tab{{position:absolute;top:0;right:90px;padding:22px 26px 16px;font-family:'Mono';font-size:24px;letter-spacing:2px;color:#fff;border-radius:0 0 10px 10px}}
.w{{position:absolute;left:170px;right:90px;top:150px}}
.no{{font-family:'Mono';font-size:26px;letter-spacing:2px;color:{MUTED}}} .no b{{background:{INK};color:#F6F1E6;padding:4px 12px;font-weight:500;margin-right:12px}}
h1{{font-weight:700;font-size:92px;line-height:1.05;letter-spacing:-1.5px;margin-top:36px}}
h2{{font-weight:700;font-size:70px;line-height:1.08;letter-spacing:-1.2px;margin-top:30px}}
.hl{{position:relative;white-space:nowrap;display:inline-block;isolation:isolate}}
.hl:before{{content:"";position:absolute;z-index:-1;left:0;right:0;bottom:.06em;height:.40em;background:{hl};border-radius:3px}}
.hand{{font-family:'Hand';font-weight:700;color:{RED};line-height:1.1}}
.p{{font-size:36px;line-height:1.4;color:#3A4560;font-weight:500}}
.fig{{position:absolute;background:#fff;box-shadow:0 2px 0 #D9CFB8;border:2px solid {INK}}}
.tape{{position:absolute;width:150px;height:44px;background:rgba(255,225,106,.6);transform:rotate(-6deg)}}
.it{{display:flex;gap:26px;align-items:center;margin-top:30px;font-size:38px;line-height:1.25;font-weight:500}}
.ck{{flex:0 0 58px;height:58px;border:3px solid {INK};border-radius:6px;position:relative}}
.ck svg{{position:absolute;left:2px;top:1px}}
.foot{{position:absolute;left:170px;right:90px;bottom:56px;display:flex;justify-content:space-between;align-items:flex-end;font-family:'Mono';font-size:21px;color:{MUTED}}}
.foot b{{font-family:'Sans';font-weight:700;font-size:28px;color:{INK};display:block}}
"""
CK = f'<svg width="52" height="52" viewBox="0 0 60 60"><path d="M10 32 L25 46 L52 12" fill="none" stroke="{RED}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def doc(kose, body, foot_left, foot_right=""):
    name, tabc, hl = KOSE[kose]
    return (f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{css(hl)}</style></head><body><div class='margin'></div>"
            f"<div class='tab' style='background:{tabc}'>{name}</div>{body}"
            f"<div class='foot'><div><b>@otizmlebirlikte</b>{foot_left}</div><div>{foot_right}</div></div></body></html>")

def deney():
    toys = (f'<svg width="290" height="230" viewBox="-145 -115 290 230"><g stroke="{INK}" stroke-width="5"><rect x="-90" y="-10" width="60" height="60" fill="#F2A65A"/>'
            f'<rect x="-20" y="-10" width="60" height="60" fill="#8DB7E0"/><rect x="-55" y="-74" width="60" height="60" fill="#B9D88C"/><circle cx="86" cy="22" r="30" fill="#FFE16A"/></g></svg>')
    gp = lambda x, y, s, fl=False: (f'<g transform="translate({x} {y}) scale({-s if fl else s} {s})" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M-62 6 C-64 -30 -20 -44 14 -40 C40 -60 78 -44 76 -14 C80 6 60 30 20 32 C-20 36 -60 34 -62 6 Z" fill="#E7B98A"/><path d="M30 -50 c4 -14 18 -14 18 -2" fill="#E7B98A"/>'
            f'<circle cx="54" cy="-18" r="4" fill="{INK}"/><path d="M-40 32 v12 M-10 34 v12 M30 30 v12"/></g>')
    pigs = f'<svg width="320" height="230" viewBox="-160 -115 320 230">{gp(-66, 10, .8)}{gp(74, 28, .7, True)}</svg>'
    body = (f'<div class="w"><div class="no"><b>DENEY 07</b>NASIL YAPILDI?</div><h2>Her grup <span class="hl">iki kez</span> oynadı</h2></div>'
            f'<div class="fig" style="left:170px;width:360px;top:560px;height:370px;padding:22px;transform:rotate(-1deg)"><div class="tape" style="left:100px;top:-22px"></div>{toys}'
            f'<div class="hand" style="text-align:center;font-size:42px">oyuncaklar</div></div>'
            f'<div class="fig" style="left:570px;width:380px;top:560px;height:370px;padding:22px;transform:rotate(1.5deg)"><div class="tape" style="left:115px;top:-22px;transform:rotate(5deg)"></div>{pigs}'
            f'<div class="hand" style="text-align:center;font-size:42px">iki ginepig</div></div>'
            f'<div class="p" style="position:absolute;left:170px;right:90px;top:990px">Önce oyuncaklarla, sonra iki ginepigle. Her grupta bir otizmli çocuk ve iki sınıf arkadaşı vardı.</div>')
    return doc("bnd", body, "O'Haire ve ark. (2013), PLoS ONE", "2 / 5")

def rakam():
    body = (f'<div class="w"><div class="no"><b>SONUÇ</b>TERCİH</div></div>'
            f'<div style="position:absolute;left:170px;top:330px;font-weight:700;font-size:330px;letter-spacing:-10px;line-height:1">%<span class="hl">82</span></div>'
            f'<div style="position:absolute;left:170px;right:90px;top:700px;font-weight:700;font-size:62px;line-height:1.12;letter-spacing:-1px">otizmli çocuk ginepigleri oyuncaklara tercih etti</div>'
            f'<div class="hand" style="position:absolute;left:170px;top:920px;font-size:46px;transform:rotate(-3deg)">4 okul · 15 kaynaştırma sınıfı</div>'
            f'<div style="position:absolute;left:170px;right:90px;top:1060px;font-family:\'Mono\';font-size:25px;line-height:1.5;color:{MUTED}">Küçük bir çalışma: iki hayvan, çeşitli oyuncaklarla karşılaştırıldı.</div>')
    return doc("bnd", body, "O'Haire ve ark. (2013), PLoS ONE", "4 / 5")

def karsilastirma():
    col = lambda x, lab, labc, big, txt, rot: (
        f'<div class="fig" style="left:{x}px;width:380px;top:520px;height:520px;padding:30px 30px;transform:rotate({rot}deg)">'
        f'<div style="font-family:\'Mono\';font-size:24px;letter-spacing:2px;color:{labc}">{lab}</div>'
        f'<div style="font-weight:700;font-size:54px;line-height:1.08;margin-top:22px;letter-spacing:-.5px">{big}</div>'
        f'<div class="p" style="font-size:31px;margin-top:22px">{txt}</div></div>')
    body = (f'<div class="w"><div class="no"><b>MİT Mİ?</b>AĞIRLIKLI YELEK</div><h2>Yelek çocuğu <span class="hl">sakinleştirir</span> mi?</h2></div>'
            + col(170, "✕ SANILAN", RED, "Yelek dikkati toplar", "Ağırlık hissi çocuğu yerinde tutar ve sakinleştirir.", -1)
            + col(580, "✓ BULUNAN", "#2F7F86", "Çoğu çalışmada fark yok", "Yelekli ve yeleksiz dönemlerde davranış benzerdi.", 1.2)
            + f'<div class="hand" style="position:absolute;left:470px;top:1090px;font-size:44px;transform:rotate(-2deg)">7 çalışmanın derlemesi</div>')
    return doc("bnd", body, "Stephenson &amp; Carter (2009), JADD", "2 / 5")

def ipucu():
    body = (f'<div class="w"><div class="no"><b>İPUCU 12</b>ÖVGÜ</div></div>'
            f'<div style="position:absolute;left:190px;right:120px;top:300px;height:640px;background:#FFD9AE;transform:rotate(-2deg);box-shadow:0 14px 22px rgba(80,60,30,.18);padding:56px 54px">'
            f'<div class="tape" style="left:300px;top:-24px;background:rgba(255,255,255,.55)"></div>'
            f'<div style="font-weight:700;font-size:74px;line-height:1.06;letter-spacing:-1.2px">Övgünüz davranışı söylesin</div>'
            f'<div style="margin-top:44px;font-size:36px;line-height:1.3;color:#7A4B22;font-family:\'Mono\'">✕ "Aferin!"</div>'
            f'<div style="margin-top:22px;font-size:40px;line-height:1.3;font-weight:600">✓ "Oyuncaklarını kutuya koyman harika!"</div></div>'
            f'<div class="hand" style="position:absolute;left:170px;right:90px;top:1020px;font-size:44px;transform:rotate(-1.5deg)">çocuk neyi doğru yaptığını tam olarak duyar</div>')
    return doc("ipucu", body, "Kaynak: Hattie &amp; Timperley (2007)", "")

def kontrol():
    items = ["Sınıfın günlük akışını resimli bir çizelgeyle gösterin",
             "Gürültülü ortamlar için sakin bir köşe ayırın",
             "Yönergeleri kısa ve tek adımlı verin",
             "Bir sınıf arkadaşını oyun eşi olarak görevlendirin",
             "Aileyle haftalık kısa bir not defteri başlatın"]
    li = "".join(f'<div class="it"><div class="ck">{CK}</div><div>{t}</div></div>' for t in items)
    body = (f'<div class="w"><div class="no"><b>LİSTE</b>KAYNAŞTIRMA</div><h2>Sınıfa yeni gelen otizmli öğrenci için <span class="hl">ilk hafta</span></h2>{li}</div>'
            f'<div class="hand" style="position:absolute;left:600px;top:1150px;font-size:42px;transform:rotate(-3deg)">hepsi birden değil!</div>')
    return doc("ogretmen", body, "Öğretmen Köşesi", "1 / 3")

PAGES = {"1-deney": deney, "2-rakam": rakam, "3-karsilastirma": karsilastirma, "4-ipucu": ipucu, "5-kontrol": kontrol}

async def main():
    out = f"{HERE}/out/tipler"; os.makedirs(out, exist_ok=True); probs = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for k, fn in PAGES.items():
            hp = f"{out}/{k}.html"; open(hp, "w", encoding="utf-8").write(fn())
            await pg.goto(f"file://{hp}"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(150)
            probs += await overlap.check(pg, k)
            await pg.screenshot(path=f"{out}/{k}.png")
        await b.close()
    print("\n".join(probs) if probs else "çakışma yok")
asyncio.run(main())
