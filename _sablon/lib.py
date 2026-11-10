import os, asyncio
from playwright.async_api import async_playwright

D = os.path.dirname(os.path.abspath(__file__))
F = f"file://{D}/fonts"
font_css = ""
for w in (400, 700, 800, 900):
    font_css += f"""
@font-face{{font-family:'Nunito';font-weight:{w};src:url('{F}/nunito-latin-ext-{w}-normal.woff2') format('woff2');unicode-range:U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF;}}
@font-face{{font-family:'Nunito';font-weight:{w};src:url('{F}/nunito-latin-{w}-normal.woff2') format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD;}}"""

BASE = font_css + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px}
body{font-family:'Nunito',sans-serif;background:#FBF6EE;color:#23363A;position:relative;overflow:hidden}
.blob1{position:absolute;width:620px;height:620px;border-radius:50%;background:#DDEFEA;top:-220px;right:-200px}
.blob2{position:absolute;width:420px;height:420px;border-radius:50%;background:#FCE6D2;bottom:-170px;left:-150px}
.wrap{position:absolute;inset:0;padding:96px 90px 160px;display:flex;flex-direction:column}
.wrap.c{justify-content:center;padding-top:70px}
.tag{display:inline-block;align-self:flex-start;background:#2F7F86;color:#fff;font-weight:800;font-size:28px;padding:12px 26px;border-radius:40px}
.pill{display:inline-block;align-self:flex-start;background:#F2994A;color:#fff;font-weight:900;font-size:30px;padding:12px 28px;border-radius:40px;margin-bottom:34px}
h1{font-weight:900;font-size:92px;line-height:1.06;color:#1F5C62;margin-top:46px}
h2{font-weight:900;font-size:68px;line-height:1.1;color:#1F5C62;margin-bottom:38px}
.lead{font-size:40px;line-height:1.4;font-weight:700;color:#3C5257;margin-top:36px}
.card{background:#fff;border-radius:36px;padding:38px 44px;box-shadow:0 10px 30px rgba(31,92,98,.08);margin-bottom:26px;display:flex;gap:32px;align-items:flex-start}
.num{flex:0 0 80px;height:80px;border-radius:24px;background:#DDEFEA;color:#2F7F86;font-weight:900;font-size:40px;display:flex;align-items:center;justify-content:center}
.card h3{font-weight:900;font-size:42px;color:#1F5C62;margin-bottom:8px}
.card p{font-size:34px;line-height:1.4;color:#3C5257}
b{font-weight:800;color:#23363A}
.note{margin-top:30px;font-size:30px;line-height:1.42;color:#4E6266;background:#F3EDE2;border-radius:28px;padding:30px 36px}
.foot{position:absolute;left:90px;right:90px;bottom:50px;display:flex;justify-content:space-between;align-items:center;font-size:27px;color:#5B6E72;font-weight:700}
.foot .h{color:#2F7F86;font-weight:900}
.dots{display:flex;gap:10px}.dots i{width:14px;height:14px;border-radius:50%;background:#CFDCD9}.dots i.on{background:#2F7F86;width:38px;border-radius:8px}
.swipe{margin-top:auto;align-self:flex-start;font-size:34px;font-weight:800;color:#2F7F86}
.myth{background:#FDECEA;border-radius:36px;padding:40px 46px;margin-bottom:28px}
.fact{background:#E3F2EE;border-radius:36px;padding:40px 46px}
.lab{font-weight:900;font-size:30px;letter-spacing:1px;margin-bottom:14px}
.myth .lab{color:#C2483A}.fact .lab{color:#2F7F86}
.myth p{font-size:52px;line-height:1.3;font-weight:800;color:#5A2A24}
.fact p{font-size:38px;line-height:1.42;color:#23363A}
.big{font-weight:900;font-size:220px;line-height:1;color:#2F7F86;margin:10px 0 18px}
.biglab{font-size:42px;font-weight:800;color:#1F5C62;line-height:1.3}
.src{margin-top:60px;font-size:23px;line-height:1.45;color:#6E7F82}
.srcmini{position:absolute;left:90px;right:90px;bottom:128px;font-size:22px;color:#7A8A8D}
.ex{display:flex;flex-direction:column;gap:22px;margin-top:40px}
.ex div{border-radius:30px;padding:36px 42px;font-size:44px;line-height:1.35;font-weight:700}
.ex .no{background:#FDECEA;color:#5A2A24}.ex .yes{background:#E3F2EE;color:#1F4A4F}
.ex span{display:block;font-size:26px;font-weight:900;letter-spacing:1px;margin-bottom:6px}
.ex .no span{color:#C2483A}.ex .yes span{color:#2F7F86}
ul.list{list-style:none}
ul.list li{display:flex;gap:24px;align-items:flex-start;margin-bottom:34px;font-size:40px;line-height:1.4;color:#3C5257}
ul.list li i{flex:0 0 58px;height:58px;border-radius:50%;background:#2F7F86;color:#fff;font-style:normal;font-weight:900;font-size:30px;display:flex;align-items:center;justify-content:center}
"""

def foot(n, total):
    sig = '<div style="line-height:1.25"><span class="h">@otizmlebirlikte</span><br><span style="font-size:22px;font-weight:700">Otizm Spektrum Bozukluğu Eğitimi Uzmanı</span></div>'
    dots = "" if total == 1 else '<div class="dots">' + "".join(f'<i class="{"on" if i==n else ""}"></i>' for i in range(1, total+1)) + "</div>"
    return f'<div class="foot">{sig}{dots}</div>'

# ---- slide builders: each returns inner html (without foot)
def cover(tag, title, lead, swipe=True):
    return f'<div class="blob1"></div><div class="blob2"></div><div class="wrap"><div class="tag">{tag}</div><h1>{title}</h1><p class="lead">{lead}</p>' + ('<div class="swipe">Kaydır →</div>' if swipe else '') + '</div>'

def cards(pill, title, items, note=None):
    c = "".join(f'<div class="card"><div class="num">{k}</div><div><h3>{h}</h3><p>{p}</p></div></div>' for k,(h,p) in enumerate(items,1)) if items and isinstance(items[0], tuple) else ""
    pl = f'<div class="pill">{pill}</div>' if pill else ''
    n = f'<div class="note">{note}</div>' if note else ''
    return f'<div class="blob1"></div><div class="wrap">{pl}<h2>{title}</h2>{c}{n}</div>'

def cards_n(pill, title, items, start=1, note=None):
    c = "".join(f'<div class="card"><div class="num">{k}</div><div><h3>{h}</h3><p>{p}</p></div></div>' for k,(h,p) in enumerate(items,start))
    pl = f'<div class="pill">{pill}</div>' if pill else ''
    n = f'<div class="note">{note}</div>' if note else ''
    return f'<div class="blob1"></div><div class="wrap c">{pl}<h2>{title}</h2>{c}{n}</div>'

def myth(pill, m, f, note=None):
    n = f'<div class="note">{note}</div>' if note else ''
    return f'<div class="blob1"></div><div class="wrap c"><div class="pill">{pill}</div><div class="myth"><div class="lab">✕ MİT</div><p>{m}</p></div><div class="fact"><div class="lab">✓ GERÇEK</div><p>{f}</p></div>{n}</div>'

def stat(pill, big, lab, text, note=None):
    n = f'<div class="note">{note}</div>' if note else ''
    return f'<div class="blob1"></div><div class="wrap c"><div class="pill">{pill}</div><div class="big">{big}</div><div class="biglab">{lab}</div><p class="lead" style="font-weight:400;font-size:36px">{text}</p>{n}</div>'

def steps(tag, title, items, src=None):
    li = "".join(f'<li><i>{k}</i><div>{t}</div></li>' for k,t in enumerate(items,1))
    s = f'<div class="src"><b>Kaynaklar:</b> {src}</div>' if src else ''
    return f'<div class="blob1"></div><div class="wrap c"><div class="tag">{tag}</div><h2 style="margin-top:36px">{title}</h2><ul class="list">{li}</ul>{s}</div>'

def tip(title, text, no, yes, src):
    return f'<div class="blob1"></div><div class="blob2"></div><div class="wrap c"><div class="tag">Günün ipucu</div><h2 style="margin-top:40px;font-size:74px">{title}</h2><p class="lead" style="margin-top:0;font-weight:400;font-size:40px">{text}</p><div class="ex"><div class="no"><span>✕ BUNUN YERİNE</span>{no}</div><div class="yes"><span>✓ ŞÖYLE DENEYİN</span>{yes}</div></div></div><div class="srcmini">Kaynak: {src}</div>'

async def render(posts, outdir):
    os.makedirs(outdir, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for slug, slides in posts.items():
            for i, body in enumerate(slides, 1):
                html = f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{BASE}</style></head><body>{body}{foot(i, len(slides))}</body></html>"
                hp = f"{outdir}/{slug}-{i}.html"
                open(hp, "w", encoding="utf-8").write(html)
                await pg.goto(f"file://{hp}")
                await pg.evaluate("document.fonts.ready")
                await pg.wait_for_timeout(150)
                await pg.screenshot(path=f"{outdir}/{slug}-{i}.jpg", type="jpeg", quality=88)
                # overflow check
                ov = await pg.evaluate("(()=>{const w=document.querySelector('.wrap');return w? w.scrollHeight>w.clientHeight : false})()")
                if ov: print("OVERFLOW", slug, i)
        await b.close()
