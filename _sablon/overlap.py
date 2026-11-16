"""Metin çakışması denetimi: sayfadaki yazı kutularının birbirine ya da sayfa dışına taşmasını ölçer."""
JS = r"""
(() => {
  const W = innerWidth, H = innerHeight, out = [];
  const els = [...document.querySelectorAll('body *')].filter(e => {
    if (['STYLE','SCRIPT','svg','g','circle','path','line'].includes(e.tagName)) return false;
    const own = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    const op = parseFloat(getComputedStyle(e).opacity);
    return own && op > 0.05;
  });
  const texts = [...document.querySelectorAll('svg text')];
  const all = [...els, ...texts].map(e => {
    let r;
    if (e.tagName === 'text') r = e.getBoundingClientRect();
    else {
      const rg = document.createRange(); rg.selectNodeContents(e); const b = rg.getBoundingClientRect();
      const fs = parseFloat(getComputedStyle(e).fontSize) || 0, ins = fs * 0.12;   // yazı tipi kutusunun boş üst/alt payı
      r = {left: b.left, right: b.right, top: b.top + ins, bottom: b.bottom - ins, width: b.width, height: Math.max(0, b.height - 2*ins)};
    }
    return {e, r, t: e.textContent.trim().slice(0, 40)};
  }).filter(o => o.r.width > 2 && o.r.height > 2);
  for (const o of all) if (o.r.left < -1 || o.r.top < -1 || o.r.right > W + 1 || o.r.bottom > H + 1) out.push('TAŞMA: ' + o.t);
  for (let i = 0; i < all.length; i++) for (let j = i + 1; j < all.length; j++) {
    const a = all[i], b = all[j];
    if (a.e.contains(b.e) || b.e.contains(a.e)) continue;
    const ox = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left);
    const oy = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
    const mh = Math.min(a.r.height, b.r.height);
    if (ox > 4 && oy > Math.max(6, mh * 0.25)) out.push('ÇAKIŞMA: "' + a.t + '" ↔ "' + b.t + '"');
  }
  // görsel ikonlar (svg g) ile metinler
  const icons = [...document.querySelectorAll('svg g.pp, svg g.pop')].map(g => g.getBoundingClientRect()).filter(r => r.width > 2);
  for (const o of all) for (const r of icons) {
    const ox = Math.min(o.r.right, r.right) - Math.max(o.r.left, r.left);
    const oy = Math.min(o.r.bottom, r.bottom) - Math.max(o.r.top, r.top);
    if (ox > 4 && oy > 4) { out.push('İKON ÇAKIŞMASI: "' + o.t + '"'); break; }
  }
  return out;
})()
"""
async def check(pg, label=""):
    issues = await pg.evaluate(JS)
    for i in issues: print(f"[{label}] {i}")
    return issues
