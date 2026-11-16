Gönderi şablonu. `lib.py` tasarım bileşenlerini (cover, cards_n, myth, stat, steps, tip) içerir; `posts.py` bir haftalık örnek.
Çalıştırma: `pip install playwright pillow --break-system-packages`, Chrome/Chromium gerekir (`/usr/bin/google-chrome`), sonra `python3 posts.py`.
Çıktı: `posts/<slug>-<n>.jpg` + `posts/manifest.json`. Görseller repoda `YYYY-MM-DD-<slug>/<n>.jpg` yoluna konur.

## Kasım 2026 eklemeleri
- `overlap.py`: Metin çakışması/taşma denetimi. `reels_bnd.py` her sahnenin son karesinde otomatik çalıştırır; çakışma varsa video üretilmez. Görsel gönderilerde de `await check(pg)` çağır.
- Köşe renkleri (aynı şablon, değişen ana renk) — `series_demo.py`:
  Bilim Ne Diyor? #2F7F86/#1F5C62/#DDEFEA · Günün İpucu #E07B39/#A8501B/#FCE6D2 · Veli Köşesi #7A62B5/#4F3D85/#E9E3F6 · Öğretmen Köşesi #3F7FBF/#24568A/#DFEAF6
- Ek düzenler — `layouts.py`: deney şeması, tek rakam (koyu zemin), karşılaştırma (Sanılan/Bulunan), "Sence?" sorusu.
- Hareketli şema örnekleri: `series_demo.py` (kulaktan kulağa zinciri), `reel_pact.py` (grup + döngü + zaman çizelgesi sahneleri; reels_bnd'yi exec ile kullanır).
