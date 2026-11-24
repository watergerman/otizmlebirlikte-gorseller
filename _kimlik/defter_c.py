"""Araştırma defteri carousel sayfa oluşturucuları. Kullanım: from defter_c import *; render_set(slug, [html,...], outdir)"""
import os, sys, asyncio
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(f"{HERE}/sayfa_tipleri.py", encoding="utf-8").read().rsplit("asyncio.run(main())", 1)[0])

BOOK = (f'<div style="position:absolute;left:170px;bottom:150px;display:flex;align-items:center;gap:14px;font-weight:700;font-size:32px;color:{INK}">'
        f'<svg width="30" height="38" viewBox="0 0 30 38"><path d="M3 3h24v32l-12-9-12 9z" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/></svg>Sonra dönmek için kaydet</div>')

def p_kartlar(kose, no, label, title, cards, note="", lead="", foot="", page=""):
    n = len(cards); cols = 2 if n in (2, 4) else 1
    html = ""
    if cols == 2:
        for k, c in enumerate(cards):
            x = 170 if k % 2 == 0 else 570; y = 560 + (k // 2) * 250; w = 360 if k % 2 == 0 else 380
            rot = [-1.2, 1.0, .8, -1][k % 4]
            html += (f'<div class="fig" style="left:{x}px;width:{w}px;top:{y}px;height:200px;padding:28px 26px;transform:rotate({rot}deg)">'
                     f'<div class="tape" style="left:100px;top:-22px"></div><div style="font-weight:700;font-size:36px;line-height:1.16">{c}</div></div>')
        ytop = 560 + ((n + 1) // 2) * 250 + 10
    else:
        for k, c in enumerate(cards):
            y = 540 + k * 170; rot = [-1.0, .9, -.7, .6, -.9][k % 5]
            html += (f'<div class="fig" style="left:170px;right:90px;top:{y}px;padding:24px 28px;transform:rotate({rot}deg)">'
                     f'<div class="tape" style="left:-24px;top:-22px"></div><div style="font-weight:700;font-size:36px;line-height:1.16">{c}</div></div>')
        ytop = 540 + n * 170 + 10
    body = (f'<div class="w"><div class="no"><b>{no}</b>{label}</div><h2>{title}</h2>'
            + (f'<div class="p" style="margin-top:18px;font-size:32px">{lead}</div>' if lead else "") + f'</div>{html}'
            + (f'<div class="hand" style="position:absolute;left:170px;right:90px;top:{ytop}px;font-size:42px;transform:rotate(-2deg)">{note}</div>' if note else ""))
    return doc(kose, body, foot, page)

def p_rakam(kose, no, label, title, big, note="", small="", foot="", page=""):
    fs = 300 if len(big) <= 4 else (200 if len(big) <= 7 else 140)
    body = (f'<div class="w"><div class="no"><b>{no}</b>{label}</div><h2>{title}</h2></div>'
            f'<div style="position:absolute;left:170px;right:90px;top:560px;font-weight:700;font-size:{fs}px;letter-spacing:-6px;line-height:1"><span class="hl">{big}</span></div>'
            + (f'<div class="hand" style="position:absolute;left:170px;right:90px;top:{560+fs+40}px;font-size:44px;transform:rotate(-2deg)">{note}</div>' if note else "")
            + (f'<div class="p" style="position:absolute;left:170px;right:90px;top:{560+fs+170}px;font-size:31px">{small}</div>' if small else ""))
    return doc(kose, body, foot, page)

def p_karsilastirma(kose, no, label, title, sanilan, bulunan, note="", foot="", page=""):
    col = lambda x, lab, labc, txt, rot: (
        f'<div class="fig" style="left:{x}px;width:380px;top:520px;height:470px;padding:30px;transform:rotate({rot}deg)">'
        f'<div style="font-family:\'Mono\';font-size:24px;letter-spacing:2px;color:{labc}">{lab}</div>'
        f'<div style="font-weight:600;font-size:38px;line-height:1.22;margin-top:22px">{txt}</div></div>')
    body = (f'<div class="w"><div class="no"><b>{no}</b>{label}</div><h2>{title}</h2></div>'
            + col(170, "✕ SANILAN", RED, sanilan, -1) + col(580, "✓ BULUNAN", "#2F7F86", bulunan, 1.2)
            + (f'<div class="hand" style="position:absolute;left:170px;right:90px;top:1050px;font-size:42px;transform:rotate(-2deg)">{note}</div>' if note else ""))
    return doc(kose, body, foot, page)

def p_kontrol(kose, no, label, title, items, limit="", foot="", page="", book=False, note="", note_title=""):
    li = "".join(f'<div class="it"><div class="ck">{CK}</div><div>{t}</div></div>' for t in items)
    body = (f'<div class="w"><div class="no"><b>{no}</b>{label}</div><h2>{title}</h2>{li}'
            + (f'<div style="font-family:\'Mono\';font-size:23px;line-height:1.5;color:{MUTED};margin-top:40px">{limit}</div>' if limit else "")
            + f'</div>' + (BOOK if book else "")
            + (f'<div class="fig" style="left:170px;right:90px;top:965px;padding:24px 30px;transform:rotate(-.8deg)"><div class="tape" style="left:-24px;top:-22px"></div>'
               f'<div class="hand" style="font-size:40px">{note_title}</div><div class="p" style="font-size:31px;margin-top:4px">{note}</div></div>' if note else ""))
    return doc(kose, body, foot, page)

def p_soru(kose, question, kunye="", foot="", page=""):
    body = (f'<div class="w"><div class="no"><b>SİZE SORUMUZ</b>YORUMLARDA BULUŞALIM</div>'
            f'<h1 style="margin-top:60px;font-size:78px">{question}</h1></div>'
            f'<div class="fig" style="left:170px;width:330px;top:830px;padding:34px;transform:rotate(-2deg);text-align:center"><div class="tape" style="left:90px;top:-22px"></div>'
            f'<div style="font-weight:700;font-size:58px">Evet</div></div>'
            f'<div class="fig" style="left:560px;width:330px;top:830px;padding:34px;transform:rotate(1.6deg);text-align:center"><div class="tape" style="left:90px;top:-22px"></div>'
            f'<div style="font-weight:700;font-size:58px">Hayır</div></div>'
            + (f'<div style="position:absolute;left:170px;right:90px;top:1040px;font-family:\'Mono\';font-size:23px;line-height:1.5;color:{MUTED}">{kunye}</div>' if kunye else "")
            + BOOK)
    return doc(kose, body, foot, page)

def p_not(kose, no, label, title, note, kunye="", foot="", page=""):
    """Yapışkan not sayfası (Günün İpucu tek görsel)."""
    body = (f'<div class="w"><div class="no"><b>{no}</b>{label}</div></div>'
            f'<div style="position:absolute;left:190px;right:120px;top:300px;min-height:600px;background:#FFD9AE;transform:rotate(-2deg);box-shadow:0 14px 22px rgba(80,60,30,.18);padding:56px 54px">'
            f'<div class="tape" style="left:300px;top:-24px;background:rgba(255,255,255,.55)"></div>'
            f'<div style="font-weight:700;font-size:70px;line-height:1.08;letter-spacing:-1.2px">{title}</div>'
            f'<div style="margin-top:40px;font-size:40px;line-height:1.32;font-weight:500">{note}</div></div>'
            + (f'<div style="position:absolute;left:170px;right:90px;top:1060px;font-family:\'Mono\';font-size:23px;line-height:1.5;color:{MUTED}">{kunye}</div>' if kunye else ""))
    return doc(kose, body, foot, page)

async def render_set(slug, pages, outdir):
    os.makedirs(outdir, exist_ok=True); probs = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for i, html in enumerate(pages, 1):
            hp = f"{outdir}/{i}.html"; open(hp, "w", encoding="utf-8").write(html)
            await pg.goto(f"file://{hp}"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(120)
            probs += await overlap.check(pg, f"{slug}-{i}")
            # fosforlu vurgu satırda bölünmüş mü / sayfadan taşıyor mu
            bad = await pg.evaluate("""[...document.querySelectorAll('.hl')].filter(e=>{const r=e.getClientRects();const b=e.getBoundingClientRect();return r.length>1||b.right>1000}).map(e=>e.textContent)""")
            probs += [f"{slug}-{i}: VURGU SORUNU {t}" for t in bad]
            await pg.screenshot(path=f"{outdir}/{i}.jpg", type="jpeg", quality=92)
        await b.close()
    return probs
