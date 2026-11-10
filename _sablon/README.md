Gönderi şablonu. `lib.py` tasarım bileşenlerini (cover, cards_n, myth, stat, steps, tip) içerir; `posts.py` bir haftalık örnek.
Çalıştırma: `pip install playwright pillow --break-system-packages`, Chrome/Chromium gerekir (`/usr/bin/google-chrome`), sonra `python3 posts.py`.
Çıktı: `posts/<slug>-<n>.jpg` + `posts/manifest.json`. Görseller repoda `YYYY-MM-DD-<slug>/<n>.jpg` yoluna konur.
