import asyncio, json, os
from lib import *

H_GENEL = "#otizm #özeleğitim #otizmspektrumbozukluğu #otizmfarkındalığı"
P = []  # (slug, datetime, slides, caption)

def add(slug, when, slides, caption):
    P.append((slug, when, slides, caption))

# ---------- 10 Kasım Salı ----------
add("t1-yonerge", "2026-11-10T13:00:00", [tip(
    "Yönergeyi kısa ve net verin",
    "Önce dikkatini çekin: adıyla seslenin, göz hizasına inin. Sonra <b>tek</b> bir yönerge verin.",
    "“Hadi bakalım artık hazırlanalım mı, dışarısı soğuk, montunu da giyersin değil mi?”",
    "“Ali, ayakkabını giy.”",
    "Matheson &amp; Shriver (2005), <i>School Psychology Review</i>, 34(2)")],
    "Uzun ve soru şeklinde verilen yönergeler çocuğun neyi yapması gerektiğini anlamasını zorlaştırır. 🗣️\n\n✅ Önce dikkatini çekin\n✅ Tek seferde tek yönerge verin\n✅ Soru değil, net bir cümle kurun\n\nBu küçük değişiklik hem evde hem sınıfta işe yarar.\n\n" + H_GENEL + " #ebeveynlik #öğretmen")

add("c1-mitler", "2026-11-10T20:30:00", [
    cover("Mit mi gerçek mi?", "Otizm hakkında 4 yaygın yanlış", "Velilerin ve öğretmenlerin en sık duyduğu inanışları araştırmalarla karşılaştırdık."),
    myth("1 / 4", "Aşılar otizme neden olur.", "Bir milyondan fazla çocuğu kapsayan çalışmaları birleştiren bir meta-analiz, aşılarla otizm arasında <b>hiçbir ilişki bulmadı</b>. Bu iddiayı ortaya atan 1998 tarihli makale ise geri çekildi."),
    myth("2 / 4", "Otizm, ebeveynlerin soğuk ya da ilgisiz davranmasından kaynaklanır.", "Otizm nörogelişimsel bir farklılıktır. 5 ülkede 2 milyondan fazla kişiyi inceleyen bir çalışmaya göre otizm riskinin yaklaşık <b>%80'i genetik etkenlerle</b> açıklanıyor. Ebeveyn tutumu otizme neden olmaz."),
    myth("3 / 4", "Resimli kartlarla ya da tabletle iletişim kurmak konuşmayı geciktirir.", "Araştırmalar tersini gösteriyor: Destekleyici ve alternatif iletişim (DAİ) konuşmayı <b>engellemiyor</b>, bazı çocuklarda konuşmayı artırıyor."),
    myth("4 / 4", "Her otizmli çocuğun dahi düzeyinde özel bir yeteneği vardır.", "Bazı otizmli bireylerde olağanüstü bir beceri görülür, ama çoğunda görülmez. Bir çalışmada bu oran yaklaşık <b>%28</b> bulundu. Her çocuk kendi güçlü yönleriyle değerlendirilmeli."),
    steps("Özetle", "Doğru bilgi, doğru destek", [
        "Otizmin nedeni aşılar ya da ebeveyn tutumu değildir.",
        "DAİ konuşmanın önünü kesmez, destekler.",
        "Her çocuk farklıdır: etikete değil, bireysel ihtiyaca bakın."],
        src="Taylor, Swerdfeger &amp; Eslick (2014), <i>Vaccine</i>, 32(29) · Bai ve ark. (2019), <i>JAMA Psychiatry</i>, 76(10) · Millar, Light &amp; Schlosser (2006), <i>JSLHR</i>, 49(2) · Howlin ve ark. (2009), <i>Phil. Trans. R. Soc. B</i>, 364")],
    "Otizm hakkında en çok duyduğumuz 4 inanış ve araştırmaların gösterdikleri. 🔍\n\n❌ Aşılar otizme neden olur\n❌ Otizm ebeveyn tutumundan kaynaklanır\n❌ Kartla/tabletle iletişim konuşmayı geciktirir\n❌ Her otizmli çocuk dahidir\n\nHepsinin gerçeğini kaydırarak okuyun. Kaynaklar son sayfada.\n\n📌 Kaydedin, yanlış bilgiyle karşılaştığınızda paylaşın.\n\n" + H_GENEL + " #mitvegerçek #DAİ #bilim")

# ---------- 11 Kasım Çarşamba ----------
add("t2-secim", "2026-11-11T12:30:00", [tip(
    "Seçim sunun",
    "Gün içinde küçük seçimler sunmak iletişimi teşvik eder ve problem davranışları azaltabilir.",
    "“Ne yemek istiyorsun?” <span style='display:inline;font-size:28px;font-weight:400;letter-spacing:0'>(açık uçlu, cevaplaması zor)</span>",
    "“Elma mı istersin, muz mu?” <span style='display:inline;font-size:28px;font-weight:400;letter-spacing:0'>(iki seçeneği göstererek)</span>",
    "Dunlap ve ark. (1994), <i>Journal of Applied Behavior Analysis</i>, 27(3)")],
    "Seçim yapmak çocuğa kontrol duygusu verir ve iletişim kurması için doğal bir fırsat yaratır. 🍎🍌\n\nİki seçeneği gösterin, birini işaret etmesini ya da söylemesini bekleyin. Yemekte, oyunda, giyinirken… her an bir fırsat.\n\n" + H_GENEL + " #iletişim #ebeveynlik")

add("c2-gorsel-takvim", "2026-11-11T20:30:00", [
    cover("Uygulama rehberi", "Görsel takvim nasıl hazırlanır?", "Evde ve sınıfta kullanabileceğiniz 5 adımlık rehber."),
    cards_n(None, "Neden işe yarar?", [
        ("Belirsizliği azaltır", "Çocuk sırada ne olduğunu görür, geçişler kolaylaşır."),
        ("Bağımsızlığı artırır", "Sürekli sözel hatırlatma ihtiyacı azalır."),
        ("Kanıta dayalıdır", "Görsel destekler, otizmde etkililiği kanıtlanmış uygulamalar arasında yer alır.")]),
    cards_n("Adım 1–2", "Planlayın", [
        ("Rutini seçin", "Sabah hazırlığı, okul günü ya da akşam rutini gibi tek bir rutinle başlayın."),
        ("Adımlara bölün", "Rutini 3–6 kısa adıma ayırın: tuvalet → el yıkama → kahvaltı → giyinme.")], 1),
    cards_n("Adım 3–4", "Hazırlayın", [
        ("Görsel türünü seçin", "Çocuğun anlayış düzeyine göre: gerçek nesne → fotoğraf → resim → yazı."),
        ("Sıralayın", "Yukarıdan aşağıya ya da soldan sağa dizin. Biten adımlar için bir “Bitti” kutusu ekleyin.")], 3),
    cards_n("Adım 5", "Öğretin", [
        ("Birlikte kullanın", "İlk günlerde her adımda takvime birlikte bakın, sonra desteği yavaş yavaş azaltın.")], 5,
        note="<b>İpucu:</b> Takvimi her gün aynı yerde ve tutarlı şekilde kullanın. Plan değişirse kartı çocuğun gözü önünde değiştirin."),
    steps("Özetle", "Unutmayın", [
        "Basit başlayın, tek rutinle.",
        "Görselleri çocuğun seviyesine göre seçin.",
        "Tutarlılık, takvimin kendisinden daha önemlidir."],
        src="Steinbrenner ve ark. (2020), <i>Evidence-Based Practices for Children, Youth, and Young Adults with Autism</i>, NCAEP · Knight, Sartini &amp; Spriggs (2015), <i>JADD</i>, 45(1)")],
    "Görsel takvim, otizmli çocuklar için en kolay uygulanabilen ve etkililiği kanıtlanmış desteklerden biri. 🗓️\n\n5 adımda evde ya da sınıfta kendi takviminizi hazırlayın:\n1️⃣ Rutini seçin\n2️⃣ Adımlara bölün\n3️⃣ Görsel türünü seçin\n4️⃣ Sıralayın\n5️⃣ Birlikte kullanarak öğretin\n\n📌 Kaydedin, hazırlarken yanınızda olsun.\n\n" + H_GENEL + " #görseltakvim #görseldestek #özeleğitimöğretmeni")

# ---------- 12 Kasım Perşembe ----------
add("t3-once-sonra", "2026-11-12T12:30:00", [tip(
    "“Önce–Sonra” kartı kullanın",
    "Zor bir etkinliği sevdiği bir etkinliğe bağlayın ve bunu iki resimli bir kartla gösterin.",
    "“Ödevini yapmazsan tablet yok!”",
    "“Önce ödev, sonra tablet.” <span style='display:inline;font-size:28px;font-weight:400;letter-spacing:0'>(iki resmi yan yana göstererek)</span>",
    "Premack (1959), <i>Psychological Review</i>, 66(4) · Steinbrenner ve ark. (2020), NCAEP")],
    "Tehdit yerine sıralama: “Önce… sonra…” 📋➡️🎮\n\nÇocuk, sevmediği işin ardından sevdiği şeyin geleceğini görünce başlamak kolaylaşır. Kartı görselle desteklemek, sözel yönergeyi anlamakta zorlanan çocuklar için çok işe yarar.\n\n" + H_GENEL + " #öncesonra #ebeveynlik")

add("c3-yayginlik", "2026-11-12T20:30:00", [
    cover("Araştırma köşesi", "Otizm ne kadar yaygın?", "ABD'nin en kapsamlı izleme ağından en güncel veriler ve ne anlama geldikleri."),
    stat("En güncel veri", "1/31", "8 yaşındaki çocuklarda otizm tanısı (%3,2)", "ABD'de 16 bölgede yürütülen izleme çalışmasına göre. 4 yaşında bu oran 1/34."),
    stat("Yaklaşık 20 yılda", "4,8×", "İlk izleme raporundan bu yana artış", "2000 yılındaki ilk raporda oran 1/150'ydi."),
    cards_n(None, "Diğer bulgular", [
        ("Erkeklerde daha sık", "Erkek çocuklarda kızlara göre yaklaşık 3,4 kat daha sık görülüyor."),
        ("Tanı hâlâ geç", "İlk tanının konduğu ortanca yaş 47 ay, yani 4 yaş civarı."),
        ("Bölgeler arası fark", "Oran bölgeye göre 1/103 ile 1/19 arasında değişiyor.")]),
    cards_n(None, "Artış bir salgın mı?", [
        ("Tanılama farkı", "Rapora göre bölgeler ve yıllar arasındaki farklar büyük ölçüde tanılama uygulamalarındaki farklılıkları yansıtıyor olabilir."),
        ("Daha fazla farkındalık", "Kızlarda ve daha önce az tanı alan gruplarda tanı oranı artıyor.")],
        note="<b>Türkiye için:</b> Ulusal ölçekte güncel yaygınlık verisi sınırlı. Bu rakamlar ABD'ye aittir ve doğrudan genellenemez."),
    steps("Ne anlama geliyor?", "Bizim için mesajı", [
        "Otizm sanıldığından çok daha yaygın; her sınıfta karşılaşabiliriz.",
        "Ortalama tanı yaşı hâlâ geç; erken fark etmek kritik.",
        "Veli ve öğretmen farkındalığı tanı sürecini hızlandırır."],
        src="Shaw ve ark. (2025), <i>MMWR Surveillance Summaries</i>, 74(2) · CDC ADDM Network, <i>2025 Community Report on Autism</i>")],
    "Her 31 çocuktan 1'i… 📊\n\nABD'nin en kapsamlı otizm izleme ağının en güncel raporuna göre 8 yaşındaki çocuklarda otizm oranı %3,2. Peki bu artış bir salgın mı, yoksa daha iyi tanılama mı? Ve bizim için ne anlama geliyor?\n\nKaydırarak okuyun, kaynaklar son sayfada.\n\n" + H_GENEL + " #araştırma #otizmistatistikleri #erkentanı")

# ---------- 13 Kasım Cuma ----------
add("t4-ovgu", "2026-11-13T12:30:00", [tip(
    "Övgünüz davranışı söylesin",
    "Neyi doğru yaptığını açıkça söyleyen övgü, o davranışın tekrar etme olasılığını artırır.",
    "“Aferin sana!”",
    "“Oyuncaklarını kutuya koyman harika!”",
    "Royer ve ark. (2019), <i>Remedial and Special Education</i>, 40(2)")],
    "“Aferin” güzel, ama çocuk neyi doğru yaptığını bilirse o davranışı tekrar etmesi daha olası. 👏\n\nÖvgünüze davranışın adını ekleyin: “Sıranı beklemen çok güzeldi”, “Kardeşine oyuncağını vermen harika”.\n\n" + H_GENEL + " #olumludavranış #öğretmen #ebeveynlik")

add("c4-kaynastirma", "2026-11-13T20:30:00", [
    cover("Öğretmenler için", "Sınıfınızda otizmli bir öğrenci mi var?", "Kaynaştırma sınıfında hemen uygulayabileceğiniz 6 kanıta dayalı strateji."),
    cards_n(None, "Ortamı düzenleyin", [
        ("Görsel destek kullanın", "Günlük program, kurallar ve yönergeleri resimli olarak sınıfa asın."),
        ("Geçişleri önceden haber verin", "Etkinlik değişmeden önce sözel uyarı verin ya da zamanlayıcı kullanın."),
        ("Oturma yerini planlayın", "Dikkat dağıtıcılardan uzak, öğretmene yakın bir yer seçin.")], 1),
    cards_n(None, "Öğretimi uyarlayın", [
        ("Kısa ve net yönerge verin", "Tek seferde tek yönerge verin, gerekirse görselle destekleyin."),
        ("Sakinleşme alanı oluşturun", "Öğrencinin bunaldığında kısa süre geçirebileceği sessiz bir köşe ayarlayın."),
        ("Akran desteğinden yararlanın", "Bilgilendirilmiş bir akranla eşleştirmek sosyal etkileşimi artırır.")], 4),
    cards_n("Bonus", "Yalnız değilsiniz", [
        ("Aileyle iletişim defteri tutun", "Gün içinde olanları aileyle paylaşın; evde ve okulda aynı stratejileri kullanın."),
        ("Rehberlik servisiyle çalışın", "BEP (Bireyselleştirilmiş Eğitim Programı) hedeflerini birlikte belirleyin.")],
        note="Bu stratejilerin çoğu sınıftaki tüm öğrenciler için de faydalıdır."),
    steps("Özetle", "Küçük değişiklikler, büyük fark", [
        "Görselleştirin, günü öngörülebilir kılın.",
        "Net konuşun, doğru davranışı fark edin.",
        "Aile ve uzmanlarla aynı dili konuşun."],
        src="Steinbrenner ve ark. (2020), <i>Evidence-Based Practices for Children, Youth, and Young Adults with Autism</i>, NCAEP · MEB Özel Eğitim Hizmetleri Yönetmeliği")],
    "Sınıf öğretmenleri için: Kaynaştırma öğrencinize destek olmanın 6 pratik yolu. 🏫\n\n🖼️ Görsel destek\n⏰ Geçiş uyarısı\n🪑 Oturma düzeni\n🗣️ Kısa ve net yönerge\n🧘 Sakinleşme alanı\n🤝 Akran desteği\n\n📌 Kaydedin ve öğretmen arkadaşlarınızla paylaşın.\n\n" + H_GENEL + " #kaynaştırma #sınıföğretmeni #öğretmen #BEP")

# ---------- 14 Kasım Cumartesi ----------
add("t5-gecis", "2026-11-14T12:30:00", [tip(
    "Geçişlerden önce haber verin",
    "Sevdiği bir etkinlikten ayrılmak zor olabilir. Önceden uyarı ve görsel bir zamanlayıcı geçişi kolaylaştırır.",
    "“Hadi, hemen kalkıyoruz!” <span style='display:inline;font-size:28px;font-weight:400;letter-spacing:0'>(aniden)</span>",
    "“5 dakika sonra parktan çıkıyoruz.” <span style='display:inline;font-size:28px;font-weight:400;letter-spacing:0'>(zamanlayıcıyı göstererek)</span>",
    "Steinbrenner ve ark. (2020), NCAEP (öncül temelli müdahaleler, görsel destekler)")],
    "Parktan çıkmak, tableti bırakmak, oyundan sofraya geçmek… Geçişler pek çok çocuk için zor anlardır. ⏳\n\nÖnceden haber vermek ve kalan süreyi görsel olarak göstermek, çocuğun hazırlanmasına zaman tanır.\n\n" + H_GENEL + " #geçişler #ebeveynlik")

add("c5-ofke-nobeti", "2026-11-14T20:30:00", [
    cover("Veliler için", "Öfke nöbeti anında ne yapmalı?", "Nöbet sırasında, sonrasında ve öncesinde atabileceğiniz adımlar."),
    cards_n("Nöbet sırasında", "Önce güvenlik", [
        ("Güvenliği sağlayın", "Çevredeki tehlikeli eşyaları uzaklaştırın, gerekirse alanı boşaltın."),
        ("Sakin kalın, az konuşun", "Uzun açıklamalar bu anda işe yaramaz. Kısa ve yumuşak bir ses tonu kullanın."),
        ("Nöbetle isteği vermeyin", "Ağlayınca istediği oluyorsa, nöbet bir iletişim yoluna dönüşebilir.")]),
    cards_n("Nöbetten sonra", "Not alın", [
        ("Ne oldu, ne zaman oldu?", "Nöbetten hemen önce olanı, nöbeti ve hemen sonrasını kısaca not edin (ABC kaydı)."),
        ("Örüntüyü arayın", "Birkaç kayıttan sonra tetikleyiciler belirginleşir: yorgunluk, açlık, geçişler, gürültü…")]),
    cards_n("Nöbetten önce", "Önleyin", [
        ("Günü öngörülebilir kılın", "Görsel takvim ve geçiş uyarıları belirsizliği azaltır."),
        ("İstemeyi öğretin", "“Mola”, “yardım”, “bitti” gibi istekleri sözle, kartla ya da işaretle öğretin. Buna işlevsel iletişim eğitimi denir.")]),
    steps("Ne zaman destek almalı?", "Uzmana başvurun, eğer…", [
        "Nöbetler sık ve uzun sürüyorsa,",
        "Çocuk kendine ya da başkalarına zarar veriyorsa,",
        "Denediğiniz stratejiler işe yaramıyorsa."],
        src="Steinbrenner ve ark. (2020), NCAEP · Tiger, Hanley &amp; Bruzek (2008), <i>Behavior Analysis in Practice</i>, 1(1)")],
    "Öfke nöbeti anında ne yapacağınızı bilmek, hem sizin hem çocuğunuzun işini kolaylaştırır. 💛\n\n🛡️ Sırasında: Güvenlik, sakinlik, isteği nöbetle vermemek\n📝 Sonrasında: Ne olduğunu not almak\n🧩 Öncesinde: Günü öngörülebilir kılmak ve istemeyi öğretmek\n\n📌 Kaydedin, zor anlarda hatırlatıcı olsun.\n\n" + H_GENEL + " #öfkenöbeti #problemdavranış #ebeveynlik #ABA")

# ---------- 15 Kasım Pazar ----------
add("t6-taklit", "2026-11-15T12:30:00", [tip(
    "Çocuğunuzu taklit edin",
    "Oyunda onun yaptığını taklit etmek dikkatini size çeker ve karşılıklı etkileşimin temelini atar.",
    "“Hayır, öyle değil. Arabayı böyle sür.”",
    "Arabasını çeviriyorsa siz de kendi arabanızı çevirin, çıkardığı sesi taklit edin.",
    "Ingersoll (2010), <i>JADD</i>, 40(9) · Steinbrenner ve ark. (2020), NCAEP")],
    "Oyunu yönlendirmek yerine bir süre onu takip edin. 🚗🚗\n\nÇocuğunuzun yaptığını taklit etmek, size bakmasını ve sizi fark etmesini sağlar. Bu da taklit, ortak dikkat ve iletişim becerilerinin temelidir.\n\nBu akşam taklitle ilgili ilginç bir araştırma paylaşacağız, takipte kalın.\n\n" + H_GENEL + " #oyun #taklit #ebeveynlik")

add("c6-konusma", "2026-11-15T20:30:00", [
    cover("Araştırma köşesi", "Konuşmayan çocukların kaçı konuşmaya başlıyor?", "707 otizmli okul öncesi çocuğu kapsayan yeni bir araştırmanın bulguları."),
    stat("Bulgu 1", "2/3", "Tek kelime söylemeye başladı", "Kanıta dayalı erken müdahale alan ve başlangıçta konuşmayan çocukların yaklaşık üçte ikisi."),
    stat("Bulgu 2", "1/2", "Kelimeleri birleştirmeye başladı", "Çocukların yaklaşık yarısı müdahalenin sonunda daha karmaşık dil kullanıyordu."),
    cards_n(None, "Neler fark yarattı?", [
        ("Motor taklit", "Hareketleri taklit edebilen çocukların konuşma kazanma olasılığı daha yüksekti."),
        ("Başlama yaşı ve süre", "Erken başlamak ve müdahalenin süresi önemliydi; haftalık saat sayısı belirleyici değildi."),
        ("Yöntem türü", "Farklı kanıta dayalı yaklaşımlar arasında belirgin bir fark çıkmadı.")]),
    cards_n(None, "Ya konuşmaya başlamayanlar?", [
        ("Yaklaşık üçte biri ilerleyemedi", "Bu çocukların başlangıçta bilişsel, sosyal ve taklit becerileri daha düşüktü."),
        ("İletişim yalnızca konuşma değildir", "Bu çocuklar için resimli kart ya da tablet gibi DAİ yöntemleri erkenden planlanmalı.")]),
    steps("Ne anlama geliyor?", "Veliler ve öğretmenler için", [
        "Erken başlamak önemli: “bekleyelim” demeyin.",
        "Taklit becerisini oyunla çalışın.",
        "Konuşma gelmese de iletişimi DAİ ile destekleyin."],
        src="Vivanti ve ark. (2025), <i>Journal of Clinical Child &amp; Adolescent Psychology</i>, doi:10.1080/15374416.2025.2579286")],
    "Konuşmayan otizmli çocukların kaçı erken müdahaleyle konuşmaya başlıyor? 🗣️\n\n707 çocuğu kapsayan yeni bir araştırmaya göre yaklaşık üçte ikisi tek kelime söylemeye, yaklaşık yarısı kelimeleri birleştirmeye başladı. Fark yaratan etkenlerden biri de bugün öğlen konuştuğumuz taklit becerisiydi.\n\nKaydırarak okuyun, kaynak son sayfada.\n\n" + H_GENEL + " #araştırma #erkenmüdahale #dilgelişimi #DAİ")

if __name__ == "__main__":
    out = f"{D}/posts"
    asyncio.run(render({s: sl for s, _, sl, _ in P}, out))
    json.dump([{"slug": s, "when": w, "n": len(sl), "caption": c} for s, w, sl, c in P], open(f"{out}/manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(P), "posts")
