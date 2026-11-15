"""16–22 Kasım 2026 haftası: carousel, ipucu, hikâye ve Reels üretimi.
Kullanım: python3 hafta_1622.py [posts] [stories] [reels] [stills]"""
import asyncio, json, os, sys, shutil
from playwright.async_api import async_playwright
from lib import *
import reels_bnd as R

REPO = os.path.dirname(D)
H = "#otizm #özeleğitim #otizmspektrumbozukluğu #otizmfarkındalığı #bilimnediyor"

BOOK = '<svg width="30" height="38" viewBox="0 0 30 38" style="vertical-align:-8px;margin-right:12px"><path d="M3 2h24v34l-12-9-12 9z" fill="none" stroke="#2F7F86" stroke-width="4" stroke-linejoin="round"/></svg>'
EXTRA = """
.save{margin-top:34px;font-size:30px;font-weight:800;color:#2F7F86}
.mean{border-radius:36px;padding:36px 44px;margin-bottom:26px}
.mean .lab{font-weight:900;font-size:30px;letter-spacing:1px;margin-bottom:12px}
.mean p{font-size:38px;line-height:1.38;color:#23363A}
.mean.y{background:#E3F2EE}.mean.y .lab{color:#2F7F86}
.mean.n{background:#FDECEA}.mean.n .lab{color:#C2483A}.mean.n p{color:#5A2A24}
"""

def meaning(yes, no):
    return f'<div class="blob1"></div><div class="wrap c"><div class="pill">Peki bu ne demek?</div><div class="mean y"><div class="lab">✓ NE ANLAMA GELİYOR?</div><p>{yes}</p></div><div class="mean n"><div class="lab">✕ NE ANLAMA GELMİYOR?</div><p>{no}</p></div></div>'

def final(tag, title, items, src):
    return steps(tag, title, items, src)[:-6] + f'<div class="save">{BOOK}Sonra dönmek için kaydet</div></div>'

P = []   # (folder, when, slides, caption, first_comment)
def add(folder, when, slides, caption, fc): P.append((folder, when, slides, caption, fc))

# ---------------- 16 Pazartesi ----------------
add("2026-11-16-c7-goz-deney", "2026-11-16T20:30:00", [
    cover("Bilim Ne Diyor?", "Bebeklikte göze bakma: Deney nasıl yapıldı?", "Bugünkü Reels'in ayrıntıları: <i>Nature</i>'da yayımlanan göz izleme çalışması."),
    cards_n("Deney", "Nasıl yapıldı?", [
        ("110 bebek", "59'unun otizmli bir ağabey ya da ablası vardı, 51'inin yoktu."),
        ("2. aydan 24. aya", "Bebekler 10 kez, bakıcı videoları izlerken göz izleme cihazıyla incelendi."),
        ("36. ayda tanı", "13 çocuk otizm tanısı aldı. Sayıca az olan kızlar analize alınmadı.")]),
    stat("Bulgu 1", "2–6 ay", "Göze bakma bu dönemde azalmaya başladı", "Tipik gelişen bebeklerde göze bakma ayda yaklaşık %3,6 artarken, sonradan tanı alanlarda ayda yaklaşık %4,8 azaldı."),
    stat("Bulgu 2", "½", "24. ayda göze bakma yarıya inmişti", "Şaşırtıcı olan: Bu bebekler ilk aylarda göze tipik düzeyde bakıyordu. Beceri baştan yok değildi, zamanla azaldı."),
    meaning("Otizmle ilişkili bazı farklılıklar çok erken başlayabilir. Erken dönem, gelişimin hâlâ şekillendiği bir penceredir.",
            "Bunu evde gözle ayırt edemezsiniz, bu bir tanı aracı değil. Analizdeki otizmli grup yalnızca 11 erkek bebekti."),
    final("Ne yapabilirsiniz?", "Veliler ve öğretmenler için", [
        "Gelişimle ilgili bir endişeniz varsa beklemeyin, değerlendirme isteyin.",
        "Göz temasını tek başına bir “test” gibi kullanmayın.",
        "Kardeşi otizmli olan bebeklerin gelişimini yakından izleyin."],
        "Jones &amp; Klin (2013), <i>Nature</i>, 504(7480), 427–431")],
    "Bilim Ne Diyor? 🔬 Bugünkü Reels'in ayrıntıları.\n\n110 bebek, 2. aydan 24. aya kadar 10 kez göz izleme cihazıyla incelendi. Sonradan otizm tanısı alan bebekler ilk aylarda göze tipik düzeyde bakıyordu; göze bakma 2–6. aylarda azalmaya başladı.\n\nBu bir tanı aracı değil ve örneklem küçük. Ama erken dönemin ne kadar önemli olduğunu gösteriyor.\n\nKaydırarak okuyun, kaynak son sayfada.\n\nBu bulgu sizi şaşırttı mı? Evet mi, hayır mı? 👇\n\n" + H + " #erkentanı #bebekgelişimi",
    "🔖 Sonra dönmek için kaydedin. Bebeği olan bir yakınınıza gönderebilirsiniz.")

# ---------------- 17 Salı ----------------
add("2026-11-17-c8-ilk-izlenim", "2026-11-17T20:30:00", [
    cover("Bilim Ne Diyor?", "İlk izlenim deneyi: 10 saniye yeter mi?", "Otizmli kişiler hakkında ilk izlenimler nasıl oluşuyor? Bir dizi deneyin sonuçları."),
    cards_n("Deney", "Nasıl yapıldı?", [
        ("40 yetişkin", "20'si otizmli, 20'si otizmsiz; yaş ve zekâ düzeyi eşleştirildi."),
        ("10 saniyelik kayıt", "Her birinin kısa bir konuşma kaydının ilk 10 saniyesi kullanıldı."),
        ("214 izleyici", "Kişileri sevimli, tuhaf, zeki gibi özelliklere göre puanladı; onlarla vakit geçirmek isteyip istemediğini belirtti.")]),
    stat("Bulgu 1", "10 sn", "Otizmli kişiler daha olumsuz değerlendirildi", "En büyük fark “tuhaf” bulunmada çıktı. İzleyiciler bu kişilerle sohbet etmeye ve vakit geçirmeye daha az istekliydi.",
         note="Çocuklarla yapılan bir başka deneyde 2–4 saniyelik videolar bile benzer sonuç verdi."),
    stat("Bulgu 2", "Metin", "Yalnızca yazılı metin okunduğunda fark kayboldu", "Söylenenler aynıydı. Olumsuz izlenim konuşmanın içeriğinden değil, ses ve görüntüden kaynaklanıyordu."),
    meaning("Otizmli bireylerin sosyal zorlukları yalnızca kendi becerileriyle ilgili değil. Çevrenin ilk tepkisinin de payı var.",
            "İnsanların kötü niyetli olduğu ya da otizmli kişinin değişmesi gerektiği anlamına gelmez. Kayıtlı videolar kullanıldı; katılımcıların zekâ düzeyi ortalama ve üzerindeydi."),
    final("Ne yapabilirsiniz?", "Sınıfta ve evde", [
        "İlk izlenimde durmayın; çocuğu söyledikleri ve yaptıklarıyla tanıyın.",
        "Sınıfta farklı iletişim tarzlarını konuşun.",
        "Akranlarla tanışmayı ortak ilgi alanları üzerinden kolaylaştırın."],
        "Sasson ve ark. (2017), <i>Scientific Reports</i>, 7, 40700")],
    "Bilim Ne Diyor? 🔬 İlk izlenim deneyi.\n\n214 kişi, 40 yetişkinin (yarısı otizmli) 10 saniyelik görüntüsünü puanladı. Otizmli kişiler daha olumsuz değerlendirildi ve onlarla vakit geçirme isteği daha düşüktü.\n\nAma aynı konuşmanın yalnızca yazılı metni okunduğunda fark kayboldu. Yani mesele söylenenler değil, ilk görüntüydü.\n\nKaydırarak okuyun, kaynak son sayfada.\n\nSizce ilk izlenim zamanla değişir mi? Evet mi, hayır mı? 👇\n\n" + H + " #ilkizlenim #kaynaştırma #farkındalık",
    "🔖 Kaydedin ve bir öğretmen arkadaşınızla paylaşın. Sınıfta konuşmak için güzel bir başlangıç.")

# ---------------- 18 Çarşamba ----------------
add("2026-11-18-t7-gorev-analizi", "2026-11-18T12:30:00", [tip(
    "İşi küçük adımlara bölün",
    "Büyük bir görevi tek seferde istemek yerine, adım adım ve her seferinde <b>bir</b> adım isteyin.",
    "“Odanı topla.”",
    "“Önce arabaları kutuya koy.” Bitince: “Şimdi kitapları rafa koy.”",
    "Steinbrenner ve ark. (2020), NCAEP")],
    "“Odanı topla” bir çocuk için tek bir iş değil, onlarca küçük iş demek. 🧸\n\nGörevi küçük adımlara bölmek (görev analizi), otizmde kanıta dayalı uygulamalardan biri. Her adım bitince kısa bir övgü, bir sonrakine başlamayı kolaylaştırır.\n\nSizde en zor hangisi: A) Oda toplamak B) Giyinmek C) Ödev? 👇\n\n#otizm #özeleğitim #otizmspektrumbozukluğu #otizmfarkındalığı #görevanalizi #ebeveynlik",
    "🔖 Kaydedin, bir dahaki “odanı topla” anında işinize yarasın.")

add("2026-11-18-c9-veli-egitimi", "2026-11-18T20:30:00", [
    cover("Bilim Ne Diyor?", "Veli eğitiminin etkisi 6 yıl sonra sürüyor mu?", "İngiltere'de yürütülen randomize kontrollü bir çalışmanın uzun dönem sonuçları."),
    cards_n("Deney", "Nasıl yapıldı?", [
        ("152 çocuk", "2–4 yaşında, otizm tanılı çocuklar kurayla iki gruba ayrıldı."),
        ("Veli aracılı program", "Bir gruptaki velilere, çocuklarının iletişim girişimlerini fark edip uyumlu yanıt vermek öğretildi. Diğer grup olağan hizmeti aldı."),
        ("Yaklaşık 6 yıl sonra", "121 çocuk, ortalama 10,5 yaşında yeniden değerlendirildi.")]),
    cards_n("Bulgular", "Ne bulundu?", [
        ("Belirtiler daha hafif", "Tüm takip boyunca programdaki çocuklarda otizm belirtilerinin şiddeti daha düşüktü."),
        ("Daha çok iletişim başlatma", "Bu çocuklar iletişimi genel olarak daha sık kendileri başlattı."),
        ("Velilerdeki fark kapandı", "Araştırmacılara göre çocuklardaki ilerleme kendi kendini sürdürür hâle gelmiş olabilir.")]),
    stat("Neden önemli?", "~6 yıl", "Erken müdahalede uzun dönem etkiye dair ilk randomize kanıt", "Araştırmacılar bu sonuçları, erken müdahale sonrası belirtilerde uzun dönem azalmayı gösteren ilk bulgular olarak tanımlıyor."),
    meaning("Veliler çocuğun gelişiminde güçlü bir rol oynayabilir ve bu beceriler öğrenilebilir.",
            "Otizm “geçmedi”. Etkiler orta düzeydeydi; dil ve kaygı gibi alanlarda fark bulunmadı. Çocukların yaklaşık %20'sine yeniden ulaşılamadı."),
    final("Ne yapabilirsiniz?", "Evde", [
        "Çocuğunuzun bakışını, sesini, işaretini bir iletişim girişimi olarak görün.",
        "Ona uyumlu yanıt verin: yönlendirmek yerine eşlik edin.",
        "Veli eğitimi programları hakkında uzmanınıza danışın."],
        "Pickles ve ark. (2016), <i>The Lancet</i>, 388(10059), 2501–2509")],
    "Bilim Ne Diyor? 🔬 Veli eğitiminin uzun dönem etkisi.\n\n152 otizmli çocuk kurayla iki gruba ayrıldı. Bir gruptaki velilere, çocuklarının iletişim girişimlerini fark edip onlara uyumlu yanıt vermek öğretildi. Yaklaşık 6 yıl sonra bu çocuklarda belirtilerin şiddeti daha düşüktü.\n\nOtizm geçmedi ve her alanda fark çıkmadı. Ama velinin rolünün ne kadar güçlü olabileceğini gösteriyor.\n\nKaydırarak okuyun, kaynak son sayfada.\n\nHiç veli eğitimine katıldınız mı? Evet mi, hayır mı? 👇\n\n" + H + " #velieğitimi #erkenmüdahale #ebeveynlik",
    "🔖 Kaydedin ve emek veren bir veliye gönderin. Yaptıklarının boşa olmadığını bilsin.")

# ---------------- 19 Perşembe ----------------
add("2026-11-19-c10-video-model", "2026-11-19T20:30:00", [
    cover("Uygulama rehberi", "Video model: İzleyerek öğrenmek", "Araştırmalarla desteklenen bu yöntemi evde ve sınıfta nasıl kullanabilirsiniz?"),
    cards_n("Nedir?", "İki türü var", [
        ("Video model", "Çocuk, hedef beceriyi bir yetişkinin ya da akranın yaparken çekilmiş kısa videosunu izler."),
        ("Kendini model alma", "Çocuk, beceriyi başarıyla yaparken çekilmiş kendi videosunu izler.")]),
    stat("Araştırma", "23", "çalışmayı birleştiren bir meta-analiz", "Bu yöntemler otizmli çocuk ve gençlerde beceri kazanımını destekledi. Kazanımlar zamanla korundu, farklı kişilere ve ortamlara taşındı."),
    cards_n("Adım 1–3", "Hazırlayın", [
        ("Tek beceri seçin", "Diş fırçalama, selam verme ya da sıra bekleme gibi."),
        ("Adımlara bölün", "Beceriyi kısa ve net adımlara ayırın."),
        ("Kısa çekin", "Gereksiz ayrıntı olmadan yalnızca beceriyi gösterin.")]),
    cards_n("Adım 4–5", "Uygulayın", [
        ("Birlikte izleyin", "Beceriyi yapmadan hemen önce videoyu birlikte izleyin."),
        ("Deneme fırsatı verin", "İzledikten sonra denemesini bekleyin, başarısını övün.")], 4),
    final("Özetle", "Unutmayın", [
        "Bir seferde tek beceri.",
        "Kısa ve net bir video.",
        "İzle, dene, övgüyle pekiştir."],
        "Bellini &amp; Akullian (2007), <i>Exceptional Children</i>, 73(3), 264–287 · Steinbrenner ve ark. (2020), NCAEP")],
    "Anlatmak yerine göstermek: Video model. 🎬\n\n23 çalışmayı birleştiren bir meta-analize göre otizmli çocuk ve gençler, kısa videolardan yeni beceriler öğrenebiliyor. Üstelik kazanımlar zamanla korunuyor ve farklı ortamlara taşınıyor.\n\n5 adımda evde ya da sınıfta nasıl uygulayacağınızı kaydırarak okuyun.\n\nİlk hangi beceriyi denerdiniz? A) Diş fırçalama B) Selam verme C) Sıra bekleme 👇\n\n" + H + " #videomodel #görseldestek #özeleğitimöğretmeni",
    "🔖 Kaydedin, videoyu çekerken adımlar yanınızda olsun.")

# ---------------- 20 Cuma ----------------
add("2026-11-20-c11-kaynasma", "2026-11-20T20:30:00", [
    cover("Bilim Ne Diyor?", "Kim kiminle daha iyi kaynaşıyor?", "Çift empati araştırmasının devamı: otizmli, otizmsiz ve karma ikililer."),
    cards_n("Deney 1", "Nasıl yapıldı?", [
        ("72 yetişkin", "Otizmli, otizmsiz ve karma (biri otizmli, biri değil) ikililer oluşturuldu."),
        ("Ortak görevler", "İkililer birlikte kule yaptı, hikâye paylaştı."),
        ("Kendi puanları", "Her görevden sonra kaynaşmayı kolaylık, keyif ve samimiyet gibi ölçütlerle puanladılar.")]),
    stat("Bulgu 1", "Karma", "ikililer kendilerini en az kaynaşmış hissetti", "Otizmli ikililer de otizmsiz ikililer de karma ikililere göre daha yüksek kaynaşma bildirdi."),
    cards_n("Deney 2", "Dışarıdan nasıl görünüyor?", [
        ("78 izleyici", "Yarısı otizmli, yarısı otizmsizdi. İkililerin 2 dakikalık sohbet videolarını izlediler."),
        ("Bilmeden puanladılar", "Kimin otizmli olduğunu bilmiyorlardı."),
        ("Sonuç", "En yüksek kaynaşma puanı otizmli ikililere, en düşük puan karma ikililere verildi.")]),
    meaning("Zorluk tek bir kişide değil, farklı iletişim tarzlarının buluşmasında olabilir. Bu, “çift empati” fikrini destekliyor.",
            "Otizmli bireylerin yalnızca otizmlilerle arkadaş olması gerektiği anlamına gelmez. Örneklem küçüktü, katılımcıların çoğu kadındı ve eşlerinin tanısını biliyorlardı."),
    final("Ne yapabilirsiniz?", "Sınıfta ve evde", [
        "Otizmli çocuğun benzer iletişim tarzındaki akranlarla da buluşabileceği ortamlar yaratın.",
        "Karma gruplarda uyumu tek tarafa yüklemeyin; karşılıklı anlamayı öğretin.",
        "Sosyal başarıyı ilişkinin kalitesine göre değerlendirin."],
        "Crompton ve ark. (2020), <i>Frontiers in Psychology</i>, 11, 586171")],
    "Bilim Ne Diyor? 🔬 Çift empati araştırmasının devamı.\n\nOtizmli, otizmsiz ve karma ikililer birlikte görev yaptı ve sohbet etti. Kimin otizmli olduğunu bilmeyen 78 izleyici, en yüksek kaynaşma puanını otizmli ikililere verdi. En düşük puan karma ikililerdeydi.\n\nYani zorluk tek bir kişide değil, iki farklı iletişim tarzının buluşmasında olabilir.\n\nKaydırarak okuyun, kaynak son sayfada.\n\nBu sonucu tahmin eder miydiniz? Evet mi, hayır mı? 👇\n\n" + H + " #çiftempati #kaynaştırma #iletişim",
    "🔖 Kaydedin ve bir öğretmenle paylaşın. Sınıfta akran ilişkilerine yeni bir bakış.")

# ---------------- 21 Cumartesi ----------------
add("2026-11-21-t8-hareket", "2026-11-21T12:30:00", [tip(
    "Hareket molası verin",
    "Hareket ve egzersiz, otizmde kanıta dayalı uygulamalar arasında yer alıyor. Masa başı bir işten önce kısa bir hareket molası deneyin.",
    "“Otur ve bitirene kadar kalkma.”",
    "“Önce 10 kez zıplayalım, sonra masaya geçelim.”",
    "Steinbrenner ve ark. (2020), NCAEP")],
    "Bazen dikkat için önce biraz hareket gerekir. 🤸\n\nHareket ve egzersiz, otizmde kanıta dayalı uygulamalardan biri. Ödevden ya da masa başı etkinlikten önce kısa bir zıplama, yürüyüş ya da top oyunu deneyin.\n\nSizin favori hareket molanız hangisi? A) Zıplama B) Yürüyüş C) Top oyunu 👇\n\n#otizm #özeleğitim #otizmspektrumbozukluğu #otizmfarkındalığı #hareket #ebeveynlik #öğretmen",
    "🔖 Kaydedin, ödev saatinden önce hatırlayın.")

add("2026-11-21-c12-yapboz", "2026-11-21T20:30:00", [
    cover("Bilim Ne Diyor?", "Yapboz parçası ne çağrıştırıyor?", "Otizmin en bilinen sembollerinden biri hakkında bir çağrışım deneyi."),
    cards_n("Deney", "Nasıl yapıldı?", [
        ("400 yetişkin", "Çalışmaya çevrim içi olarak katıldılar."),
        ("Hızlı eşleştirme testi", "Yapboz parçalarını ve benzer geometrik şekilleri olumlu ve olumsuz kelimelerle eşleştirdiler."),
        ("Serbest çağrışım", "Yapboz parçası ve geometrik şekil için akıllarına gelen ilk 5 kelimeyi yazdılar.")]),
    stat("Bulgu 1", "%50", "yapboz çağrışımlarının olumsuz olma oranı", "Geometrik şekillerde bu oran %33'tü. Sık geçen çağrışımlar: eksiklik, kusur, tuhaflık, “bir parçanın eksik olması”."),
    cards_n("Bulgu 2", "Hızlı testte ne çıktı?", [
        ("Olumsuzla daha hızlı", "Katılımcılar yapboz parçalarını olumsuz kelimelerle daha hızlı ve daha doğru eşleştirdi."),
        ("Logolarda da var", "Bu eğilim otizm logolarında da görüldü; genel yapboz parçalarında biraz daha güçlüydü.")]),
    meaning("Semboller, niyetten bağımsız olarak belirli çağrışımlar taşıyabilir.",
            "Sembolü kullananların kötü niyetli olduğunu göstermez. Çalışma davranışı değil çağrışımları ölçtü; katılımcılar çoğunlukla ABD'deki çevrim içi gönüllülerdi."),
    final("Ne yapabilirsiniz?", "Materyal hazırlarken", [
        "Kullandığınız sembolün ne çağrıştırdığını düşünün.",
        "Mümkünse otizmli bireylerin görüşünü sorun.",
        "Sembolden çok mesaja odaklanın: kabul ve destek."],
        "Gernsbacher ve ark. (2018), <i>Autism</i>, 22(2), 118–125")],
    "Bilim Ne Diyor? 🔬 Yapboz parçası ne çağrıştırıyor?\n\n400 yetişkinle yapılan bir deneyde, yapboz parçası için yazılan çağrışımların yarısı olumsuzdu: eksiklik, kusur, tuhaflık. Geometrik şekillerde bu oran %33'tü.\n\nBu, sembolü kullananların kötü niyetli olduğu anlamına gelmez. Ama sembollerin taşıdığı mesajı düşünmeye değer.\n\nKaydırarak okuyun, kaynak son sayfada.\n\nYapboz sembolünü siz kullanıyor musunuz? Evet mi, hayır mı? 👇\n\n" + H + " #yapboz #sembol #farkındalık",
    "🔖 Kaydedin; okulda afiş ya da materyal hazırlarken hatırlayın.")

# ---------------- 22 Pazar ----------------
add("2026-11-22-c13-kanita-dayali", "2026-11-22T20:30:00", [
    cover("Bilim Ne Diyor?", "Otizmde kanıta dayalı 28 uygulama", "Kapsamlı bir derlemenin sonuçları ve hemen başlayabileceğiniz 5 uygulama."),
    stat("Derleme", "28", "kanıta dayalı uygulama belirlendi", "1990–2017 arasında yayımlanan 972 araştırma tarandı. Uygulamalar doğumdan 22 yaşa kadar olan bireyleri kapsıyor."),
    cards_n("Hemen başlayın", "5 kolay uygulama", [
        ("Model olma", "Beceriyi önce siz gösterin, sonra çocuğun denemesini bekleyin."),
        ("Bekleme süresi", "Yardım etmeden önce birkaç saniye bekleyin; yardımı zamanla geciktirin."),
        ("Sosyal öyküler", "Yeni bir durumu, kısa bir öyküyle (gerekirse resimlerle) önceden anlatın.")]),
    cards_n("Hemen başlayın", "5 kolay uygulama", [
        ("Akran destekli öğretim", "Sınıf arkadaşlarına, otizmli akranlarıyla oyun ve iletişim kurmanın yollarını öğretin."),
        ("Davranışsal ivme", "Zor bir istekten önce, çocuğun kolayca yapabileceği 2–3 kısa istekte bulunun.")], 4),
    meaning("Bir yöntem önerildiğinde, arkasında araştırma olup olmadığını sormak için güçlü bir başvuru listesi.",
            "Listede olmayan her yöntemin işe yaramadığı anlamına gelmez. Listedekiler de her çocuğa aynı şekilde uymaz."),
    final("Ne yapabilirsiniz?", "Veliler ve öğretmenler için", [
        "Size önerilen yöntemin bu listede olup olmadığını sorun.",
        "Uygulamayı çocuğun ihtiyacına ve hedefine göre seçin.",
        "İlerlemeyi düzenli olarak gözlemleyip kaydedin."],
        "Steinbrenner ve ark. (2020), <i>Evidence-Based Practices for Children, Youth, and Young Adults with Autism</i>, NCAEP")],
    "Bilim Ne Diyor? 🔬 Otizmde etkisi kanıtlanmış kaç uygulama var?\n\n972 araştırmayı tarayan kapsamlı bir derleme 28 kanıta dayalı uygulama belirledi. Görsel destekler, model olma, video model, veli aracılı müdahale bunlardan bazıları.\n\nEvde ve sınıfta hemen başlayabileceğiniz 5 tanesini kaydırarak okuyun.\n\nBu listeyi daha önce duymuş muydunuz? Evet mi, hayır mı? 👇\n\n" + H + " #kanıtadayalıuygulama #özeleğitimöğretmeni #ebeveynlik",
    "🔖 Kaydedin; size bir yöntem önerildiğinde bu listeye dönün. Bir öğretmen ya da veliyle paylaşabilirsiniz.")

# ================= REELS =================
REELS = {
 "2026-11-17-r7-ilk-izlenim": ("2026-11-17T17:30:00", [
  R.s_hook("Otizmli biri hakkındaki ilk izlenim kaç saniyede oluşuyor?"),
  R.s_stat("10 sn", "Bu kadarlık görüntüde otizmli kişiler daha olumsuz değerlendirildi", "214 izleyici, 40 yetişkin (yarısı otizmli)"),
  R.s_points("Şaşırtıcı olan", ["Aynı konuşmanın yalnızca yazılı metni okunduğunda fark kayboldu.", "Yani mesele söylenenler değil, ilk görüntüydü."]),
  R.s_not("Otizmli kişinin değişmesi gerektiği anlamına gelmez. Katılımcılar yetişkinlerdi ve kayıtlı videolar kullanıldı."),
  R.s_act("SINIFTA VE EVDE", "İlk izlenimde durmayın. Çocuğa, söyledikleri ve yaptıklarıyla tanınma fırsatı verin.", "Sizce ilk izlenim değişir mi? Evet mi, hayır mı?", "Sasson ve ark. (2017), <i>Scientific Reports</i>, 7"),
 ], "Bilim Ne Diyor? 🔬\n\nBir deneyde 214 kişi, 40 yetişkinin (yarısı otizmli) yalnızca 10 saniyelik görüntüsünü izledi. Otizmli kişiler daha olumsuz değerlendirildi; izleyiciler onlarla sohbet etmeye daha az istekliydi.\n\nŞaşırtıcı olan: Aynı konuşmanın yazılı metni okunduğunda fark kayboldu. Yani mesele söylenenler değil, ilk görüntüydü.\n\n👉 İlk izlenimde durmayın. Çocuğa, söyledikleri ve yaptıklarıyla tanınma fırsatı verin.\n\nBu akşam 20:30'da deneyin ayrıntıları carousel'de.\n\nSizce ilk izlenim zamanla değişir mi? Evet mi, hayır mı? 👇\n\nKaynak: Sasson ve ark. (2017), Scientific Reports\n\n" + H + " #ilkizlenim #kaynaştırma #farkındalık",
  "🔖 Kaydedin ve bir öğretmen arkadaşınıza gönderin. Bu bulguyu herkesin bilmesi gerek."),
 "2026-11-18-r8-veli-egitimi": ("2026-11-18T17:30:00", [
  R.s_hook("Veliye verilen eğitim, 6 yıl sonra hâlâ fark yaratabilir mi?"),
  R.s_stat("~6 yıl", "sonra çocuklar yeniden değerlendirildi", "152 çocuktan 121'i, ortalama 10,5 yaşında"),
  R.s_points("Bulgu", ["Veli eğitimi alan gruptaki çocuklarda belirtilerin şiddeti daha düşüktü.", "Araştırmacılara göre çocuklardaki ilerleme kendi kendini sürdürmüş olabilir."]),
  R.s_not("Otizm “geçmedi”. Etkiler orta düzeydeydi; dil ve kaygı gibi alanlarda fark bulunmadı."),
  R.s_act("NE YAPABİLİRSİNİZ?", "Çocuğunuzun iletişim girişimlerini fark edin ve onlara eşlik edin. Bu beceri öğrenilebilir.", "Veli eğitimine katıldınız mı? Evet mi, hayır mı?", "Pickles ve ark. (2016), <i>The Lancet</i>, 388"),
 ], "Bilim Ne Diyor? 🔬\n\nİngiltere'de 152 otizmli çocuk kurayla iki gruba ayrıldı. Bir gruptaki velilere, çocuklarının iletişim girişimlerini fark edip onlara uyumlu yanıt vermek öğretildi.\n\nYaklaşık 6 yıl sonra bu gruptaki çocuklarda otizm belirtilerinin şiddeti daha düşüktü. Araştırmacılara göre ilerleme kendi kendini sürdürür hâle gelmiş olabilir.\n\nOtizm geçmedi; dil ve kaygı gibi alanlarda fark bulunmadı. Ama velinin rolü küçümsenmemeli.\n\n👉 Çocuğunuzun bakışını, sesini, işaretini bir iletişim girişimi olarak görün ve ona eşlik edin.\n\nHiç veli eğitimine katıldınız mı? Evet mi, hayır mı? 👇\n\nKaynak: Pickles ve ark. (2016), The Lancet\n\n" + H + " #velieğitimi #erkenmüdahale #ebeveynlik",
  "🔖 Kaydedin ve emek veren bir veliye gönderin."),
 "2026-11-19-r9-video-model": ("2026-11-19T17:30:00", [
  R.s_hook("Bir beceriyi anlatmak yerine videoyla göstermek işe yarar mı?"),
  R.s_stat("23", "çalışmayı birleştiren bir meta-analiz", "Video model ve kendini video ile model alma incelendi"),
  R.s_points("Bulgu", ["Çocuklar ve gençler videodan yeni beceriler öğrendi.", "Kazanımlar zamanla korundu, farklı kişilere ve ortamlara taşındı."]),
  R.s_not("Çocuk, hedef beceriyi kısa bir videoda bir modelin ya da kendisinin yaparken izler. Sonra aynısını dener.", "VİDEO MODEL NEDİR?"),
  R.s_act("DENEYİN", "Tek bir beceriyi kısa bir videoya çekin. Birlikte izleyin, sonra birlikte deneyin.", "Hiç denediniz mi? Evet mi, hayır mı?", "Bellini &amp; Akullian (2007), <i>Exceptional Children</i>, 73(3)"),
 ], "Anlatmak yerine göstermek işe yarar mı? 🎬\n\n23 çalışmayı birleştiren bir meta-analize göre otizmli çocuk ve gençler, kısa videolardan yeni beceriler öğrenebiliyor. Kazanımlar zamanla korunuyor ve farklı kişilere, ortamlara taşınıyor.\n\n👉 Diş fırçalama gibi tek bir beceriyi kısa bir videoya çekin. Birlikte izleyin, sonra birlikte deneyin.\n\nBu akşam 20:30'da adım adım uygulama rehberi carousel'de.\n\nHiç denediniz mi? Evet mi, hayır mı? 👇\n\nKaynak: Bellini & Akullian (2007), Exceptional Children\n\n" + H + " #videomodel #görseldestek #ebeveynlik",
  "🔖 Kaydedin; videoyu çekmeden önce tekrar izleyin."),
 "2026-11-20-r10-kaynasma": ("2026-11-20T17:30:00", [
  R.s_hook("Otizmli iki kişi sohbet ettiğinde dışarıdan nasıl görünüyor?"),
  R.s_points("Deney", ["Otizmli, otizmsiz ve karma ikililer 2 dakika sohbet etti.", "78 izleyici, kimin otizmli olduğunu bilmeden kaynaşmayı puanladı."]),
  R.s_stat("1.", "En yüksek kaynaşma puanını otizmli ikililer aldı", "En düşük puan karma ikililere verildi"),
  R.s_not("Zorluk tek bir kişide değil, iki farklı iletişim tarzının buluşmasında olabilir. Örneklem küçük; çoğu katılımcı kadın.", "NE ANLAMA GELİYOR?"),
  R.s_act("SINIFTA", "Karma gruplarda uyumu tek tarafa yüklemeyin. Karşılıklı anlamayı öğretin.", "Bu sonucu tahmin eder miydiniz? Evet mi, hayır mı?", "Crompton ve ark. (2020), <i>Frontiers in Psychology</i>, 11"),
 ], "Bilim Ne Diyor? 🔬 Çift empati araştırmasının devamı.\n\nOtizmli, otizmsiz ve karma ikililer 2 dakika sohbet etti. Kimin otizmli olduğunu bilmeyen 78 izleyici videoları puanladı.\n\nEn yüksek kaynaşma puanı otizmli ikililere, en düşük puan karma ikililere verildi.\n\nBu, zorluğun tek bir kişide değil, iki farklı iletişim tarzının buluşmasında olabileceğini düşündürüyor. Örneklem küçük ve bulgunun tekrarlanması gerekiyor.\n\n👉 Karma gruplarda uyumu tek tarafa yüklemeyin, karşılıklı anlamayı öğretin.\n\nBu sonucu tahmin eder miydiniz? Evet mi, hayır mı? 👇\n\nKaynak: Crompton ve ark. (2020), Frontiers in Psychology\n\n" + H + " #çiftempati #kaynaştırma #iletişim",
  "🔖 Kaydedin ve bir öğretmen arkadaşınıza gönderin."),
 "2026-11-21-r11-yapboz": ("2026-11-21T17:30:00", [
  R.s_hook("Yapboz parçası sembolü insanlara ne çağrıştırıyor?"),
  R.s_stat("400", "yetişkinle bir çağrışım deneyi", "Hızlı eşleştirme testi ve akla gelen ilk kelimeler incelendi"),
  R.s_points("Bulgu", ["Yapboz parçaları olumsuz kelimelerle daha hızlı eşleştirildi.", "Çağrışımların %50'si olumsuzdu (şekillerde %33): eksik, kusurlu, tuhaf."]),
  R.s_not("Sembolü kullananların kötü niyetli olduğunu göstermez. Katılımcılar çoğunlukla ABD'deki çevrim içi gönüllülerdi."),
  R.s_act("NE YAPABİLİRSİNİZ?", "Materyal hazırlarken sembollerin ne çağrıştırdığını düşünün. Mümkünse otizmli bireylere sorun.", "Yapboz sembolünü kullanıyor musunuz? Evet mi, hayır mı?", "Gernsbacher ve ark. (2018), <i>Autism</i>, 22(2)"),
 ], "Bilim Ne Diyor? 🔬\n\nYapboz parçası, otizmin en bilinen sembollerinden biri. Peki insanlara ne çağrıştırıyor?\n\n400 yetişkinle yapılan bir deneyde yapboz parçaları olumsuz kelimelerle daha hızlı eşleştirildi. Yazılan çağrışımların yarısı olumsuzdu: eksiklik, kusur, tuhaflık. Geometrik şekillerde bu oran %33'tü.\n\nBu, sembolü kullananların kötü niyetli olduğunu göstermez. Ama sembollerin taşıdığı mesajı düşünmeye değer.\n\n👉 Afiş ya da materyal hazırlarken mümkünse otizmli bireylerin görüşünü sorun.\n\nYapboz sembolünü kullanıyor musunuz? Evet mi, hayır mı? 👇\n\nKaynak: Gernsbacher ve ark. (2018), Autism\n\n" + H + " #yapboz #sembol #farkındalık",
  "🔖 Kaydedin ve okulda materyal hazırlayan bir öğretmenle paylaşın."),
 "2026-11-22-r12-kanita-dayali": ("2026-11-22T17:30:00", [
  R.s_hook("Otizmde etkisi kanıtlanmış kaç uygulama var?"),
  R.s_stat("28", "kanıta dayalı uygulama", "1990–2017 arasında yayımlanan 972 araştırma tarandı"),
  R.s_points("Listede neler var?", ["Görsel destekler, model olma, video model", "Veli aracılı müdahale, akran destekli öğretim, hareket ve egzersiz"]),
  R.s_not("Listede olmayan her yöntemin işe yaramadığı anlamına gelmez. Listedekiler de her çocuğa aynı şekilde uymaz."),
  R.s_act("NE YAPABİLİRSİNİZ?", "Size önerilen yöntemin bu listede olup olmadığını sorun. Seçimi çocuğun ihtiyacına göre birlikte yapın.", "Bu listeyi biliyor muydunuz? Evet mi, hayır mı?", "Steinbrenner ve ark. (2020), NCAEP"),
 ], "Bilim Ne Diyor? 🔬\n\nOtizmde etkisi kanıtlanmış kaç uygulama var? 1990–2017 arasında yayımlanan 972 araştırmayı tarayan kapsamlı bir derleme 28 kanıta dayalı uygulama belirledi.\n\nGörsel destekler, model olma, video model, veli aracılı müdahale, akran destekli öğretim ve hareket bunlardan bazıları.\n\nListede olmayan her yöntem işe yaramaz demek değil; listedekiler de her çocuğa aynı şekilde uymaz.\n\n👉 Size bir yöntem önerildiğinde, arkasında araştırma olup olmadığını sorun.\n\nBu akşam 20:30'da hemen başlayabileceğiniz 5 uygulama carousel'de.\n\nBu listeyi biliyor muydunuz? Evet mi, hayır mı? 👇\n\nKaynak: Steinbrenner ve ark. (2020), NCAEP\n\n" + H + " #kanıtadayalıuygulama #özeleğitimöğretmeni #ebeveynlik",
  "🔖 Kaydedin; bir yöntem önerildiğinde bu listeyi hatırlayın."),
}

# ================= HİKÂYELER (1080×1920) =================
SCSS = font_css + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
body{font-family:'Nunito',sans-serif;background:#FBF6EE;color:#23363A;position:relative}
.b1{position:absolute;width:900px;height:900px;border-radius:50%;background:#DDEFEA;top:-380px;right:-320px}
.b2{position:absolute;width:640px;height:640px;border-radius:50%;background:#FCE6D2;bottom:-260px;left:-240px}
.sig{position:absolute;left:96px;top:190px;font-size:38px;font-weight:900;color:#2F7F86}
.wrap{position:absolute;left:96px;right:96px;top:330px;bottom:360px;display:flex;flex-direction:column;justify-content:center}
.tag{align-self:flex-start;background:#2F7F86;color:#fff;font-weight:900;font-size:40px;padding:16px 34px;border-radius:50px}
.tag.o{background:#F2994A}
h1{font-weight:900;font-size:96px;line-height:1.08;color:#1F5C62;margin-top:44px}
h2{font-weight:900;font-size:74px;line-height:1.12;color:#1F5C62;margin-top:44px}
.sub{font-size:44px;line-height:1.38;font-weight:700;color:#3C5257;margin-top:36px}
.opt{display:flex;gap:30px;align-items:center;background:#fff;border-radius:40px;padding:38px 44px;margin-top:30px;box-shadow:0 10px 30px rgba(31,92,98,.08);font-size:50px;font-weight:800;line-height:1.25}
.opt i{flex:0 0 96px;height:96px;border-radius:30px;background:#DDEFEA;color:#2F7F86;font-style:normal;font-weight:900;font-size:52px;display:flex;align-items:center;justify-content:center}
.opt.ok{background:#2F7F86;color:#fff}.opt.ok i{background:#fff}
.hint{margin-top:50px;font-size:38px;font-weight:800;color:#F2994A}
.cta{margin-top:60px;align-self:flex-start;background:#1F5C62;color:#fff;font-size:42px;font-weight:900;padding:24px 40px;border-radius:50px}
.src{margin-top:44px;font-size:30px;color:#6E7F82;font-weight:700;line-height:1.4}
.li{display:flex;gap:26px;align-items:flex-start;background:#fff;border-radius:36px;padding:30px 36px;margin-top:24px;font-size:40px;line-height:1.32;font-weight:700;color:#23363A;box-shadow:0 10px 30px rgba(31,92,98,.08)}
.li b{flex:0 0 70px;height:70px;border-radius:22px;background:#DDEFEA;color:#2F7F86;font-weight:900;font-size:36px;display:flex;align-items:center;justify-content:center}
"""
def sframe(inner): return f'<div class="b1"></div><div class="b2"></div><div class="sig">@otizmlebirlikte</div><div class="wrap">{inner}</div>'
def s_announce(kind, title, sub): return sframe(f'<div class="tag">Yeni {kind}</div><h1>{title}</h1><p class="sub">{sub}</p><div class="cta">Profilde, şimdi →</div>')
def s_q(q, a, b): return sframe(f'<div class="tag o">Sence?</div><h2>{q}</h2><div class="opt"><i>A</i><span>{a}</span></div><div class="opt"><i>B</i><span>{b}</span></div><p class="hint">Cevabını DM\'den yaz · Doğru cevap yarın hikâyede</p>')
def s_a(q, a, b, ok, expl, src):
    oa, ob = ("ok", "") if ok == "A" else ("", "ok")
    return sframe(f'<div class="tag">Dünün cevabı</div><h2 style="font-size:60px">{q}</h2><div class="opt {oa}"><i>A</i><span>{a}</span></div><div class="opt {ob}"><i>B</i><span>{b}</span></div><p class="sub" style="font-size:40px">{expl}</p><p class="src">Kaynak: {src}</p>')
def s_week(items):
    li = "".join(f'<div class="li"><b>{k}</b><div>{t}</div></div>' for k, t in enumerate(items, 1))
    return sframe(f'<div class="tag">Bilim Ne Diyor?</div><h2 style="margin-bottom:16px">Bu haftanın 4 bulgusu</h2>{li}<p class="hint" style="color:#2F7F86">Hepsi kaynaklarıyla profilde</p>')

Q1 = ("İnsanlar otizmli biri hakkındaki ilk izlenimi ne kadar sürede oluşturuyor?", "Birkaç dakikada", "Birkaç saniyede")
Q2 = ("Velilere verilen iletişim eğitiminin etkisi yaklaşık 6 yıl sonra ölçüldü. Sence?", "Etki kaybolmuştu", "Bazı etkiler sürüyordu")
Q3 = ("Kimin otizmli olduğunu bilmeyen izleyicilere göre hangi ikililer sohbette daha çok kaynaşıyor?", "Otizmli + otizmli", "Otizmli + otizmsiz")
Q4 = ("400 yetişkin, yapboz parçası için akla gelen ilk kelimeleri yazdı. Bunların ne kadarı olumsuzdu?", "Yaklaşık %10", "Yaklaşık %50")

S = [  # (folder, when, html)
 ("2026-11-16-hikaye", "2026-11-16T12:00:00", s_q(*Q1)),
 ("2026-11-16-hikaye", "2026-11-16T17:35:00", s_announce("Reels", "Bebeklikte göze bakma", "Sonradan otizm tanısı alan bebeklerde ne değişiyor? Akşam 20:30'da deneyin ayrıntıları carousel'de.")),
 ("2026-11-17-hikaye", "2026-11-17T11:30:00", s_a(*Q1, "B", "Bir deneyde 10 saniyelik görüntüler, başka bir deneyde 2–4 saniyelik videolar bile yetti. Ayrıntılar bugün 17:30'da Reels'te.", "Sasson ve ark. (2017), <i>Scientific Reports</i>")),
 ("2026-11-17-hikaye", "2026-11-17T12:00:00", s_q(*Q2)),
 ("2026-11-17-hikaye", "2026-11-17T17:35:00", s_announce("Reels", "İlk izlenim deneyi", "10 saniyelik görüntüde ne oldu, yazılı metinde ne değişti? Akşam 20:30'da ayrıntılar carousel'de.")),
 ("2026-11-18-hikaye", "2026-11-18T11:30:00", s_a(*Q2, "B", "Yaklaşık 6 yıl sonra, programdaki çocuklarda otizm belirtilerinin şiddeti daha düşüktü. Ayrıntılar bugün 17:30'da Reels'te.", "Pickles ve ark. (2016), <i>The Lancet</i>")),
 ("2026-11-18-hikaye", "2026-11-18T17:35:00", s_announce("Reels", "Veli eğitimi 6 yıl sonra", "152 çocuk, kurayla iki grup, yaklaşık 6 yıllık takip. Akşam 20:30'da ayrıntılar carousel'de.")),
 ("2026-11-19-hikaye", "2026-11-19T12:00:00", s_q(*Q3)),
 ("2026-11-19-hikaye", "2026-11-19T17:35:00", s_announce("Reels", "Video model: İzleyerek öğrenmek", "Anlatmak yerine göstermek işe yarar mı? Akşam 20:30'da 5 adımlık uygulama rehberi.")),
 ("2026-11-20-hikaye", "2026-11-20T11:30:00", s_a(*Q3, "A", "78 izleyici, en yüksek kaynaşma puanını otizmli ikililere, en düşük puanı karma ikililere verdi. Ayrıntılar bugün 17:30'da Reels'te.", "Crompton ve ark. (2020), <i>Frontiers in Psychology</i>")),
 ("2026-11-20-hikaye", "2026-11-20T12:00:00", s_q(*Q4)),
 ("2026-11-20-hikaye", "2026-11-20T17:35:00", s_announce("Reels", "Kim kiminle daha iyi kaynaşıyor?", "Çift empati araştırmasının devamı. Akşam 20:30'da ayrıntılar carousel'de.")),
 ("2026-11-21-hikaye", "2026-11-21T11:30:00", s_a(*Q4, "B", "Çağrışımların %50'si olumsuzdu (geometrik şekillerde %33): eksiklik, kusur, tuhaflık. Ayrıntılar bugün 17:30'da Reels'te.", "Gernsbacher ve ark. (2018), <i>Autism</i>")),
 ("2026-11-21-hikaye", "2026-11-21T17:35:00", s_announce("Reels", "Yapboz parçası ne çağrıştırıyor?", "400 yetişkinle bir çağrışım deneyi. Akşam 20:30'da ayrıntılar carousel'de.")),
 ("2026-11-22-hikaye", "2026-11-22T12:00:00", s_week([
    "İlk izlenim 10 saniyede oluşabiliyor; yazılı metinde fark kayboluyor.",
    "Veli eğitiminin izleri yaklaşık 6 yıl sonra da görülebiliyor.",
    "Kaynaşmada zorluk, farklı iletişim tarzlarının buluşmasında olabilir.",
    "Yapboz çağrışımlarının yarısı olumsuz."])),
 ("2026-11-22-hikaye", "2026-11-22T17:35:00", s_announce("Reels", "Kanıta dayalı 28 uygulama", "972 araştırmadan çıkan liste. Akşam 20:30'da hemen başlayabileceğiniz 5 uygulama.")),
]

async def render_posts():
    tmp = f"{D}/_out"; os.makedirs(tmp, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for folder, _, slides, _, _ in P:
            od = f"{REPO}/{folder}"; os.makedirs(od, exist_ok=True)
            for i, body in enumerate(slides, 1):
                html = f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{BASE}{EXTRA}</style></head><body>{body}{foot(i, len(slides))}</body></html>"
                hp = f"{tmp}/x.html"; open(hp, "w", encoding="utf-8").write(html)
                await pg.goto(f"file://{hp}"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(120)
                ov = await pg.evaluate("(()=>{const w=document.querySelector('.wrap');if(!w)return false;const r=[...w.querySelectorAll('*')].map(e=>e.getBoundingClientRect().bottom);return Math.max(0,...r) > 1350-150 || w.scrollHeight>w.clientHeight})()")
                if ov: print("OVERFLOW", folder, i)
                await pg.screenshot(path=f"{od}/{i}.jpg", type="jpeg", quality=90)
        pg2 = await b.new_page(viewport={"width": 1080, "height": 1920})
        cnt = {}
        for folder, when, html in S:
            od = f"{REPO}/{folder}"; os.makedirs(od, exist_ok=True)
            hp = f"{tmp}/s.html"
            open(hp, "w", encoding="utf-8").write(f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{SCSS}</style></head><body>{html}</body></html>")
            await pg2.goto(f"file://{hp}"); await pg2.evaluate("document.fonts.ready"); await pg2.wait_for_timeout(120)
            ov = await pg2.evaluate("(()=>{const w=document.querySelector('.wrap');return w.scrollHeight>w.clientHeight})()")
            name = when[11:16].replace(":", "")
            if ov: print("OVERFLOW story", folder, name)
            await pg2.screenshot(path=f"{od}/{name}.jpg", type="jpeg", quality=90)
        await b.close()

async def render_reels(stills, only):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": R.W, "height": R.H})
        for folder, (_, sc, _, _) in REELS.items():
            if only and folder not in only: continue
            await R.build(folder, sc, pg, stills)
            if not stills:
                os.makedirs(f"{REPO}/{folder}", exist_ok=True)
                shutil.copy(f"{D}/reels/{folder}/reel.mp4", f"{REPO}/{folder}/reel.mp4")
        await b.close()

def manifest():
    m = []
    for folder, when, slides, cap, fc in P:
        m.append({"type": "POST", "folder": folder, "when": when, "media": [f"{i}.jpg" for i in range(1, len(slides)+1)], "text": cap, "firstComment": fc})
    for folder, (when, sc, cap, fc) in REELS.items():
        m.append({"type": "REEL", "folder": folder, "when": when, "media": ["reel.mp4"], "text": cap, "firstComment": fc, "dur": round(sum(d for d, _ in sc), 1)})
    for folder, when, _ in S:
        m.append({"type": "STORY", "folder": folder, "when": when, "media": [when[11:16].replace(":", "") + ".jpg"]})
    m.sort(key=lambda x: x["when"])
    json.dump(m, open(f"{D}/hafta_1622.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    a = sys.argv[1:]
    only = [x for x in a if x.startswith("2026")]
    if "posts" in a: asyncio.run(render_posts())
    if "reels" in a or "stills" in a: asyncio.run(render_reels("stills" in a, only))
    manifest()
