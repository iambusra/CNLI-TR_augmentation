from annotator import annotate_in_bulk




default_fields = {"id": None, "form": None, "lemma": None, "upos": None, "xpos": None,
           "feats": None, "head": None, "deprel": None, "deps": None, "misc": None}


##### PUNCTUATION #####
forms_to_annotate =  [","]
annotation = default_fields.copy()
annotation["lemma"] = ","
annotation["upos"] = "PUNCT"
annotation["xpos"] = "Comma"
annotation["deprel"] = "punct"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["."]
annotation = default_fields.copy()
annotation["lemma"] = "."
annotation["upos"] = "PUNCT"
annotation["xpos"] = "Stop"
annotation["deprel"] = "punct"
annotation["misc"] = "SpacesAfter=\\n"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["?"]
annotation = default_fields.copy()
annotation["lemma"] = "?"
annotation["upos"] = "PUNCT"
annotation["xpos"] = "Ques"
annotation["deprel"] = "punct"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

##### PROPNs #####
forms_to_annotate =  ["Abidin","Abraham","Ali","Astrid","Asude","Ayla","Ayşe","ayşe","Ayşenur","Aysu","Banu","Barış","Batu","Belma","Bener","Berrin","Buse","Büşra","Canan","Cansu","Cenk","Ceylan","Cüneyt","Deniz","deniz","Eda","Elif","Emre","Ender","Enes","Eren","Filiz","Gaye","Gizem","Gönül","Gülay","Gülin","Gülsüm","Gürsel","Güzide","Hakan","Hale","Halime","Hamiyet","Hilal","Hüseyin","Jale","Janset","Jülide","Kenan","Kerem","Kübra","Kurumi","Leyla","Mehmet","Melahat","Müge","Muharrem","Müjdat","Mustafa","Nil","Nur","Oğuz","Orkun","öykü","Öykü","Ozan","Özlem","Pelin","Recep","Remziye","Rüstem","Seda","Selin","Şeyda","Şeyma","Süheyla","Şule","Sunay","Süreyya","Tijen","Turan","Uygar","Vedat","Yağız","Yaprak","Yaren","yetkin","Yetkin","Yiğit","Züleyha","Zülfikar","Allah","Anıl","Atacan","Aysun","Bensu","Beren","Berk","Berke","Beyza","Buket","Burak","Çağla","Can","Cankat","Cem","Ceyhun","Çolpan","Doğanay","Doruk","Dündar","Erkan","Esra","Evren","Fatma","Fatoş","Ferhunde","Feride","Fikriye","Goldilocks","Gözde","Handan","Helin","Hülagü","Hülya","Ilgın","İlke","İmge","Itır","Kamil","Köroğlu","Lale","Leman","Melike","Mercan","Mikaela","Mırnav","Naciye","Nazan","Nazım","Nermin","Nino","Nuran","Olcay","Oya","Özge","Reyhan","Semra","Şermin","Suat","Tahsin","Talha","Teoman","Uve","Yelda","Yeliz","Yusuf","Zerrin","Zeynep","Can","Hülya","Doruk","Cem","Yelda","Nermin","Lale","Özge","Yeliz","Serra","Aysun","Oya","Arzu","Yeşim","Furkan","Cankat","Şermin",   "Naz","Ahmet","Meltem","Yeter","Fazıl","Yücel","Hüsnü","Nisa","Ufuk","Kaan","Saygın","Hürrem","Hediye","Venüs","Zebercet","Tevfik","Hande","Gamze","Tuna","Akif","Efe","Ilgın","Erçin","Serdar","Ulrika","Fatih","Emilia","Azra","Nazlı","Selim","Ünzile","Miray","Gamze","Fahriye","Şükran","Perihan","Berivan","Ercan","Nazenin","Bülent","Çiğdem","Derin","Tülay","Mahir","Aybala","Irmak","Cemre","Rezzak","Ceyda","Yıldız","Azra","Utku","Fikri","Buğra","Ayten","Zahide","Hilmican","Rumet","Nihat","Henrik","Nazen","Ezgi","Erdem","Dilara","Baran","Halide","İnci","Nergis","Harun","Şuayip","Feriha","Benan","Berkay","Didem","Sude","Asena","Melis","Halil","Fırat","Gökçe","Duygu","Yurdanur","Behice","Soner","Tarık","Bade","Nezahat","Yurdakul","Niyazi","Murat","Muhterem","Gürkan","Mükerrem","Zümran","Neslihan","Çiçek","Ünsal","Narin","Sadık","Aysima","Aslı","Şakir","Defne","Erdem","Özden","Tilbe","Mete","Mahmut","Nilay","Mert","Tolga","Ziynet","Dudu","Pınar","Ferit","Hikmet","Sezen","Ege","İlke","Suat","Gözde","Yelda","Fatma","Tahsin","Helin","Burak","Nazan"]
annotation = default_fields.copy()
annotation["upos"] = "PROPN"
annotation["feats"] = "Case=Nom|Number=Sing|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["Abidin'in","Ali'nin","Astrid'in","Asude'nin","Ayla'nın","Ayşe'nin","Ayşe'ninki","ayşe'ninkiler","Ayşe'ninkiler","Ayşenur'un","Aysu'nun","aysu'nunki","Aysu'nunki","Banu'nun","Barış'ın","Batu'nun","Belma'nın","Bener'in","buğra'nınki","Buğra'nınki","Buse'nin","Büşra'nın","büşra'nınki","Büşra'nınki","Canan'ın","Cansu'nun","Cüneyt'in","Deniz'in","Eda'nın","Emre'nin","Ender'in","Enes'in","Eren'in","Filiz'in","Gaye'nin","Gizem'in","Gönül'ün","Gülay'ın","Gülin'in","Gülsüm'ün","Gürsel'in","Güzide'nin","Hakan'ın","Hale'nin","Halime'nin","Hilal'in","Hüseyin'in","Jale'nin","Janset'in","Jülide'nin","Kenan'ın","Kerem'in","Kübra'nın","Kurumi'nin","lale'ninki","Lale'ninki","Leyla'nın","leyla'nınki","Leyla'nınki","Mehmet'in","Melahat'in","Müge'nin","Muharrem'in","Müjdat'ın","Mustafa'nın","Nil'in","Nur'un","Oğuz'un","Orkun'un","Ozan'ın","Özlem'in","Pelin'in","Recep'in","Remziye'nin","Rüstem'in","Seda'nın","Selin'in","Şeyda'nın","Şeyma'nın","Süheyla'nın","Şule'nin","Sunay'ın","Süreyya'nın","Tijen'in","Turan'ın","Uygar'ın","Vedat'ın","Yağız'ın","Yaprak'ın","Yaren'in","Yiğit'in","Züleyha'nın","Zülfikar'ın","Cenk'in","Arda'nın","Furkan’ın","zeynep'inki","Can'ın","Hülya'nın","Doruk'un","Cem'in","Nermin'in","Lale'nin","Özge'nin","Yeliz'in","Serra'nın","Aysun'un","Oya'nın","Arzu'nun","Yeşim'in","Furkan'ın","Yusuf'un","Cankat'ın","Köroğlu'nun","Şermin'in","Naz'ın","Ahmet'in","Meltem'in","Yeter'in","Fazıl'ın","Yücel'in","Hüsnü'nün","Nisa'nın","Ufuk'un","Kaan'ın","Saygın'ın","Hürrem'in","Hediye'nin","Venüs'ün","Zebercet'in","Tevfik'in","Hande'nin","Gamze'nin","Tuna'nın","Akif'in","Efe'nin","Ilgın'ın","Erçin'ın","Serdar'ın","Ulrika'nın","Fatih'in","Emilia'nın","Azra'nın","Nazlı'nın","Selim'in","Ünzile'nin","Miray'ın","Gamze'nin","Fahriye'nin","Şükran'ın","Perihan'ın","Berivan'ın","Ercan'ın","Nazenin'in","Bülent'in","Çiğdem'in","Derin'in","Tülay'ın","Mahir'in","Aybala'nın","Irmak'ın","Cemre'nin","Rezzak'ın","Ceyda'nın","Yıldız'ın","Azra'nın","Utku'nun","Fikri'nin","Buğra'nın","Ayten'in","Zahide'nin","Hilmican'ın","Rumet'in","Nihat'ın","Henrik'in","Nazen'in","Ezgi'nin","Dilara'nın","Baran'ın","Halide'nin","İnci'nin","Nergis'in","Harun'un","Şuayip'in","Feriha'nın","Benan'ın","Berkay'ın","Didem'in","Sude'nin","Asena'nın","Melis'in","Halil'in","Fırat'ın","Gökçe'nin","Duygu'nun","Yurdanur'un","Behice'nin","Soner'in","Tarık'ın","Bade'nin","Nezahat'in","Yurdakul'un","Niyazi'nin","Murat'ın","Muhterem'in","Gürkan'ın","Mükerrem'in","Zümran'ın","Neslihan'ın","Çiçek'in","Ünsal'ın","Narin'in","Sadık'ın","Aysima'nın","Aslı'nın","Şakir'in","Defne'nin","Erdem'in","Özden'in","Tilbe'nin","Mete'nin","Mahmut'un","Nilay'ın","Mert'in","Tolga'nın","Ziynet'in","Dudu'nun","Pınar'ın","Ferit'in","Hikmet'in","Sezen'in","Ege'nin","İlke'nin","Suat'ın","Gözde'nin","Yelda'nın","Fatma'nın","Tahsin'in","Helin'in","Burak'ın","Nazan'ın",]
annotation = default_fields.copy()
annotation["upos"] = "PROPN"
annotation["feats"] = "Case=Gen|Number=Gen|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["Goldilocks'a","Yelda'ya"]
annotation = default_fields.copy()
annotation["upos"] = "PROPN"
annotation["feats"] = "Case=Dat|Number=Gen|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["Zerrin'den","Tülay'dan"]
annotation = default_fields.copy()
annotation["upos"] = "PROPN"
annotation["feats"] = "Case=Abl|Number=Gen|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

##### NOUNs #####
#Nom
forms_to_annotate =  ["adam","aday","ajan","Akşam","akşam","alıntı","alışveris","alışveriş","an","anı","apartman","araba","arkadaş","aşık","bahçe","balık","bank","bardak","bileklik","bölüm","çanta","casus","çeşit","çocuk","davet","defter","dergi","Ders","ders","dikiş","dil","doktor","dükkan","ekmek","elbise","eşya","ev","Ev","fidan","fiyatlar","fotoğraf","göl","hata","hediye","göz","gün","hala","halı","hamak","hırsız","yolculuk","yumurta","yün","iddia","iş","katılımcı","kız","kitap","Kitap","kişi","kahvaltı","kahve","kaza","kedi","kediler","koltuk","konu","konuk","köpek","kimono","lira","makine","masa","manzara","yıldız","market","öneri","öğrenci","oduncu","mezun","mızıka","mızıkacı","mühendis","okul","müze","mülakat","müşteri","oyuncu","tren","soru","Şövalye","tamirci","tane","tatlı","tekne","tesisatçı","ülke","uzman","vapur","yangın","Para","para","park","pasta","piknik","plaj","reklamcı","resim","restoran","otel","roman","röportaj","Sağduyu","sağduyu","salon","yer","yemek","yazlık","yat","yarış","Yarış","sıvacı","sıvacılık","şirket","şarap","şarkı","satıcı","satın","sebze","servis","sevgili","şey","şoför","yardımcı","ağrı","anne","ara","aşı","aslan","astronot","ateş","avize","ay","ayıp","bağ","bahçıvan","baş","bela","belgesel","berber","bisiklet","böğürtlen","borç","boyacı","büyükelçi","cambaz","Cin","dans","dere","Deve","deyim","diken","dilim","dirhem","doktorluk","dolar","düet","düşler","düşman","el","elma","eşek","eşlik","et","Evlilik","farz","fikir","film","fincan","Fırıncı","gam","garsonluk","gece","görüş","grup","gül","hafta","Hakim","hakim","hayır","hile","horoz","imza","inşa","insan","IT","ısırık","kadın","kara","kaşif","kavanoz","keçi","keder","keyif","kimlik","kısır","kıyafet","Komite","kopya","koyun","kravat","kulübe","kumaş","kurabiye","kural","kutlama","kütüphane","madalya","makam","mektup","meyve","Müdür","muhbir","musibet","muska","müzik","oda","ödül","ölü","Ölüm","panda","parmak","Pastacı","personel","plan","puan","rüşvet","sahip","sanatçı","sandalye","şans","şarkıcı","satranç","şehir","sekreter","sene","seramik","seyahat","sigara","Sihir","sihirbaz","şiir","sorgu","söz","sporcu","su","sunum","süt","tabak","tablo","tahlil","Tambur","tasa","tavsiye","Teleferik","temsil","tenis","tepe","Terzi","teşekkür","tutam","üst","üye","uyuz","yarı","yazar","yazı","yelken","yıl","yoğurt","sabah","atasözü","Cumartesi","dost","geri","hasbihal","herkes","izleyiciyi","Kör","Organizatör","dün","hemşire","padişah","kurt","eşek","bitki","ot","deve","hayvan","içecek","dal","tepe","ara","ağız","adam","teklif","Güneş","güneş","zaman","mercimek","hikaye","çocuk","şahıs","biri","bina","biri","yarışmacı","güvenlik","Güvenlik","hasta","Hasta","çalışan","Öğretmen","öğretmen","ziyaretçi","Hırsız","sorgu","Sorgu","organizatör","Organizatör","cumartesi","elma","konuşma","Madalya","madalya","organizasyon","hastane","öğretmenlik","işletme","numara","gösteri","antrenman","kütüphane","çekmece","kelebek","sebep","yılan","sihirbaz","kaşık","hemşire","etek","toplantı","talep","tekne","modifiye","bebek","sipariş","oje","mantar","Jüri","jüri","mihmandar","Büyükelçi","büyükelçi","izleyici","şort","ayakkabı","model","nefret","öğretim","biber","kayıt","staj","fizikçi","reklam","saksı","Emlakçı","emlakçı","arzu","ilan","çikolata","Belediye","belediye","valiz","kuyumcu","altın","bambu","Altın","daktilo","kafe","şiş","iplik","bere","merak","yiyecek","tantuni","konser","üniversite","balo","kağıt","Resim","mesaj","ithalat","kombin","mum","makas","Kahvaltı","kahvaltı","makale","terapist","diploma","Alıntı","yabancı","mevzu","doping","şapka","Nefret","Mezun","İlan","ortam","aşçı","Aşçı","Düşme","düşme","heybe","Kutlama","Yazı","başvuru","Bambu","kuyumcu","hırka","şart","İthalat","zürafa","Ezan","namaz","seccade","kolye","Bahçıvan","poster","traktör","karpuz","Karpuz","mama","tatil","sirtaki","vakit","kitapçı","muhabbet","parti","domates","Şef","şef","cilt","ayna","sahil","haber","eczane","işbirliği","hissedar","kurutma","proje","inşaat","uygulama","oyuncak","Kedi","kedi","nemlendirici","prenses","keman","televizyon","ikna","dizi","dosya","çözüm","kanun","Müşteri","yardım","hayal","bilet","parfüm","yatak","böcek","oğlan","boncuk","sorun","çiçek","uçuş","ofis","Hakem","hakem","faul","oyun","Yardım","evlat","kamyonet","Öğrenci","Polis","polis","Avrupa","ziyaret","referans","görev","konferans","sinema","ağaç","Ağaç","İnsan","insan","tutuklu","nesne","varlık","Su","su","Hasbıhal","hasbıhal","Balık","Film","Konferans","kurs","sessizlik","Ziyaret",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Nom|Number=Sing|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["boklar","Eskiler","Futbolcular","öğrenciler","şeyler","Elektrikler","elektrikler","şartlar","saatler","hikayeler",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Nom|Number=Plur|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Acc
forms_to_annotate =  ["anıyı","arabayı","bölümü","dili","dükkanı","evi","fotoğrafı","halıyı","kimonoyu","koltuğu","limonu","Okulu","okulu","onu","restoranı","şarabı","şiiri","soruyu","tatlıyı","tesisatçıyı","adayı","ağacı","aleti","alışverişi","altlığı","başı","çiçeği","dağları","Deveyi","elbiseyi","eli","işi","kapıyı","kediyi","kendisini","kitabı","köpeği","kumaşı","kurabiyeyi","makaleyi","marmelatı","memuru","mercimeği","numarayı","odayı","öğrenciyi","öğretmeni","padişahı","sesi","siteyi","sürprizi","sürüyü","ülkeyi","yemeği","yemekleri","maydanozu","pandayı","pencereyi","ekmeği","kilidi","yarışmacıyı","deveyi","aşıyı","madalyayı","şüpheyi","tahlili","elmayı","kesiciyi","belgeseli","tabağı","ilanı","bisikleti","kadını","şapkayı","sınavı","ayakkabıyı","çikolatayı","daireyi","şehri","ödevi","olayı","çantayı","hikayeyi","şarkıyı","domatesi","konuyu","seccadeyi","mektubu","dersi","eczaneyi","domatesi","fidanı","şeyi","alanı",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Acc|Number=Sing|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["odunları", "evrakları","kişileri","arabaları","ağaçları","kitapları","boncukları","notaları","sorumlulukları","şeyleri",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Acc|Number=Plur|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Dat
forms_to_annotate =  ["adama","banka","bölüme","dergiye","eve","kediye","köpeğe","kuyumcuya","manzaraya","masaya","okula","müşteriye","müzeye","parka","otele","plaja","trene","yola","soruya","ağıza","antremana","başa","berbere","bilene","buraya","çekmeceye","çiçeğe","davaya","demirciye","doktora","eteğine","fırına","gazeteciye","gönlüne","gösteriye","halıya","hastaneye","hayata","işe","kadına","kulübüne","kursuna","kütüphaneye","maceraya","mahalleye","Mutfağa","nasihate","öğrenciye","sahafçıya","Taksiye","uzmana","yere","ziyaretçiye","ata","Doktoru","kurda","çıkışa","vakte","Atasözüne","atasözüne","oraya","çocuğa","restorana","sana","panoya","depresyona","derse","doğum","bahçeye","denize","konuya","otobüse","balkona","konsere","bara","Yola","yola","Balkona","Meydana","dolaba","koridora","Koridora","gazeteye","dershaneye","soruna","sınava","uçuşa","arabaya","mutfağa","öğretmene","Öğretmene","makaleye","pandaya","sinemaya","dile",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Dat|Number=Sing|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["kedilere"]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Dat|Number=Plur|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Loc
forms_to_annotate =  ["apartmanda","bahçede","bankta","derecede","dışında","fotoğrafta","gelecekte","grupta","hamakta","kahvaltıda","konuda","okulda","öneride","zamanda","salonda","restoranda","ülkede","şirkette","tatilde","mesleğinde","mutfakta","odada","ortamda","sahilde","sınıfta","treninde","yarıda","yatakta","yolda","ağaçta","arabada","balkonda","banyoda","barda","bilgisayarda","çöplükte","çukurda","dairede","departmanda","Dernekte","dışarıda","evde","fırsatta","ipte","kafede","kanepede","kırda","işte","damacanada","nişanda","yerde","filmde","otelde","stüdyoda","Salıncakta","salıncakta","heybede","yiğitte","depresyonda","üniversitede","kulüpte","kursta","ülkede","ofiste","kütüphanede","Kütüphanede","işte","İşte","sinemada","binada","şehirde","dernekte","sayıda","koridorda",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Loc|Number=Sing|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["okullarda","denizlerde","Denizlerde",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Loc|Number=Plur|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Abl
forms_to_annotate =  ["adamdan","benden","dersten","Dersten","dükkandan","dükkanından","fidanlardan","herkesten","Herkesten","kitaptan","marketten","Marketten","okuldan","önceden","pastadan","şirketten","sınıfından","tatlıdan","türden","haftasonundan","dansözden","mağazadan","nasihatten","nereden","odadan","Polisten","sınavdan","uzmandan","yardan","yaşlıdan","yoldan","ağaçtan","ağızdan","arabayla","bilgisayarla","çatalla","denizden","Gruptan","hayattan","kaşıktan","köyden","kurabiyeden","kütüphaneden","makaleden","Evden","evden","ayaktan","Pazardan","pazardan","birinden","telefondan","Telefondan","kitaptan","mevzudan","yemekten","manavdan","kadından","ortamdan","buradan","Buradan","olaydan","Buradan","Kütüphaneden","kütüphaneden","duraktan","şeyden","gitardan","gölden","Konudan","konudan","şehirden","ülkeden","havalimanından","romandan","sorudan","Bundan","bundan","yerden","polisten",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Abl|Number=Sing|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["diyarlardan","insanlardan","kişilerden","misafirlerden","Öğrencilerden","hakemlerden","hastalardan","olaylardan","havalimanlarından","yataklardan","masalardan","dergilerden",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Abl|Number=Plur|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Gen
forms_to_annotate =  ["adamın","çocuğun","dalından","ekmeğin","evden","gözlemcinin","hala'nın","halının","hırsızın","katılımcının","kişinin","kitabın","kızın","kurabiyenin","mızıkacı'nın","mızıkanın","Mızıkanın","oduncunun","Öğrencinin","öğrencinin","şeyin","sıvacının","Şövalye'nin","şunun","yerin","atın","ayının","binanın","casusun","çatalın","çiçeğin","dalın","elin","elmanın","Eşeğin","eteğin","Evlinin","evsizin","gencin","gömleğin","hemşirenin","hepsinin","hikâyenin","hizmetçinin","inişin","işin","kahvenin","kelebeğin","kötünün","Meramın","milletvekilinin","misafirin","piyadenin","politikacının","salonun","taşın","tatilcinin","tutuklunun","vaktin","yarışmacının","yarışmanın","yazarın","yılanın","ziyaretçinin","yiğidin","kimsenin","Devenin","devenin","etin","gülün","dikenin","horozun","cambazın","keçinin","tasanın","Terzinin","terzinin","parmağın","berberin","Berberin","Yarışmanın","yarışmanın","hikayenin","Doktorun","doktorun","kişinin","Jürinin","jürinin","Ajanın","ajanın","Polisin","polisin","Müdürün","müdürün","Öğretmenin","öğretmenin","Pastacının","pastacının","Fırıncının","fırıncının","üyenin","insanın","suyun","yabancının","herkesin","filmin","sporcunun","aşçının","yemeğin","Emlakçının","emlakçının","valizin","derginin","teknenin","restoranın","hayvanın","arabanın","ilanın","bisikletin","kadının","ayakkabının","makinenin","manavın","evin","bahçenin","aracın","dairenin","kıyafetin","biberin","albümün","mekanın","sözün","konunun","mektubun","yazlığın","makasın","diplomanın","tabağın","müzisyenin","bardağın","Bahçıvanın","bahçıvanın","hakemin","Hakemin","Müşterinin","müşterinin","rakibin","traktörün","uçuşun","hediyenin","mızıkacının","kuralın","oğlanın","gayrimenkulün","okulun","mevzunun","denizin","birinin","gayrimenkulun","gayrimenkulün","canlının","ortamın","dosyanın","bölümün","makalenin","nesnenin","odanın","sinemanın","kursun",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Gen|Number=Sing|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["Büyükelçilerin","doktorların","Milletvekillerinin","profesörlerin","futbolcuların","kişilerin","Milletvekillerinin","milletvekillerinin","Yemeklerin","yemeklerin","Odaların","odaların","adayların","Adayların","öğrencilerin","Öğrencilerin","Katılımcıların","katılımcıların","İşlerin","işlerin","Tatilcilerin","tatilcilerin","çatalların","Çatalların","kitapların","tutukluların","Tutukluların","politikacıların","izleyicilerin","Anıların","anıların","meyvelerin",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Gen|Number=Plur|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Inst
forms_to_annotate =  ["adamla","adayla","ihtimalle","kızla","makineyle","konukla","mezunla","mühendisle","uzmanla","dosyayla","insanla","kadınla","onunla","makasla","öğrenciyle","çikolatayla","arabayla","doktorla","daktiloyla","ayakkabıyla","konuyla","rakiple","sorunla","menajerle","muhtarla","anahtarla","hastayla","tesisatçıyla",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Inst|Number=Sing|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["kitaplarla","ayakkabılarla"]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Inst|Number=Plur|Person=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)


#Poss
forms_to_annotate =  ["Annem","arkadaşım","Arkadaşım","kardeşim","Kardeşim","Anneannem", "Benim","ablam","annem","çantam","Kuzenim","kuzenim","Kedim","kedim","babam","Babam"]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Nom|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=1"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["Annemler", ]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Nom|Number=Plur|Number[psor]=Sing|Person=3|Person[psor]=1"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["moralimi"]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Acc|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=1"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["kardeşime","Kardeşime",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Dat|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=1"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["Annemler'in",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Gen|Number=Plur|Number[psor]=Sing|Person=3|Person[psor]=1"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["kardeşimden",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Abl|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=1"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["dolabımda",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Loc|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=1"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["Arkadaşım'ın","arkadaşımın","annemin","Anneannemin","anneannemin","annemin","Kuzenimin","kuzenimin","ablamın","kardeşimin","Kardeşimin",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Gen|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=1"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["arkadaşı","hatası","bahsi","gezisi","sahibi","Sevgilisi","sevgilisi","mesleği","yolculuğu","yüzü","üyesi","oğlu","Ölüsü","ortağı","sakini","şarkısı","tamamı","turnuvası","zararı","ablası","ağrısı","ayağı","çıkışı","delisi","departmanı","dolgusu","geçidi","görevlisi","hatırı","jürisi","kızı","nesi","odası","sayısı","grubu","yılı","Yılı","tümü","tamamı","görevi","memurluğu","kursu","bilgisi","makinesi","günü","takımı","iyisi","kapağı","hissi","ajansı","arabası","sözü","Doktoru","doktoru","kanseri","kremi","kasabası","eğitimi","mühendisi","Eskisi","eskisi","suyu","cildi","türü","komşusu","Komşusu","cildi","Planı","planı","ülkesi","dikimi","uzmanlığı",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Nom|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["görevlileri","görevleri","dersleri","kaynakları",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Nom|Number=Plur|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["köpeğini","arkadaşını","işini","Annesini","arabasını","başını","beşini","gecesini","hayatını","ödevini","sevgilisini","tanesini","uçağını","varını","yoğunu","Ödevini","ödevini","tümünü","tamamını","ortağını","evini","yerini","evini","beğenisini","dönemini","komşusunu","Komşusunu","kremini","Köpeğini","köpeğini","ülkesini",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Acc|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["yazılarını","üzüntülerini","İşlerini","işlerini","Sevinçlerini","sevinçlerini","Günlerini","günlerini","Çamaşırlarını","çamaşırlarını","sırlarını","meyvelerini","fiyatlarını",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Acc|Number=Plur|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["arkadaşına","gezisine","yolculuğuna","altına", "duvarına","odasına","üstüne","yanına","yüzüne","şüphesine","inancına","departmanına","düşüncesine","inancına","kanısına","kıyafetine","evine","düğününe","başkasına","partisine","evine","Arkadaşına","Eline","eline","başına","yemeğine","kasabasına","oğluna","Oğluna","sevgilisine","kasabasına","gözüne",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Dat|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["kaynaklarına","şüphelerine",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Dat|Number=Plur|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["kitabında","Bakanlığı'nda","balkonunda","gölgesinde","gönlünde","katında","şüphesinde","Şüphesinde","döneminde","ajansında","yanında","salonunda","kasabasında","konusunda","alanında","okulunda","kapağında","türünde","dükkanında","aklında",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Loc|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["liselerinde"]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Loc|Number=Sing|Number[psor]=Plur|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["arkadaşının","kızının","görevlisinin","başkanının","birisinin","birinin","çoğunun","kitabının","hayatının","kapağının","masasının",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Gen|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["misafirlerinin","kitaplarının","resimlerinin",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Gen|Number=Plur|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["babasıyla","biriyle","annesiyle","arkadaşıyla"]
annotation = default_fields.copy().copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Inst|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["sevinçleriyle","Sevinçleriyle",]
annotation = default_fields.copy().copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Inst|Number=Plur|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["yemeğinden","tarafından","elinden","kabininden","patronundan","panosundan","ağacından","arkadaşından","üniversitesinden","ülkesinden","kanserinden","okulundan",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Abl|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["fiyatlarından",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Abl|Number=Plur|Number[psor]=Sing|Person=3|Person[psor]=3"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

###SEN
forms_to_annotate =  ["çantana",]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["feats"] = "Case=Dat|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=2"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)




##### ADJs #####
forms_to_annotate =  ["aynı","başka","Başka","Belirli","belli","bu","büyük","Büyük","esmer","Esmer","farklı","Gaddar","görkemli","Güzel","güzel","hediyelik","işsiz","kaslı","kırmızı","kızıl","mutlu","olgun","Olgun","önemli","özel","Özel","rengarenk","saçlı","şu","şüpheli","sürükleyici","tecrübeli","Tecrübeli","tüm","Uzak","uzak","üzücü","uzun","yalnız","yeni","yoğun","Yorgun","yorgun","zorunlu","Her","her","herhangi","hamile","habersiz","iyi","kaslı","kısa","kaç","önce","merkezi","mevcut","resmi","yakın","açık","Akıllı","az","başarılı","Benzersiz","boylu","bucaksız","davetsiz","deneyimli","emekli","eski","etkileyici","gizli","harika","hayran","hızlı","ilk","ışıltılı","kalabalık","kesici","Konuşkan","küçük","öbür","ödünç","organik","parlak","rahat","sahte","şaşkın","şefkatli","Şefkatli","sessiz","sıkıcı","suçlu","talihsiz","uçsuz","yalancı","Yanlış","yaşlı","yetenekli","yüksek","zeki","Fransız","uygun","öbür","öteki","spesifik","İyi","bu","şu","ortak","Ortak","yanlış","Uzun","lüks","Hamile","hamile","alışık","cam","etkileyici","kapsamlı","topuklu","siyah","lezzetli","yeşil","spor","tıpkı","gergin","acı","üstün","aşina","şık","geniş","erken","tanınmış","Yarın","yarın","akıllıca","sevimli","ponponlu","keyifli","benzer","şaşırtıcı","benzer","Gergin","Küçük","dayanıklı","sarışın","Sarışın","yaş","bazı","Bazı","zor","okullu","tarihi","kiralık","cesur","ekonomik","canlı","kullanışlı","kuru","yerel","rahatsız","sakin","kibar","hassas","yakışıklı","Portekizli","belirli","güçlü","hızlı","güvenilir","romantik","prestijli","geçen","yorucu","sevimli","yorucu","Yorucu","Farklı","farklı","Sevimli","konuşkan",]
annotation = default_fields.copy()
annotation["upos"] = "ADJ"
annotation["xpos"] = "Adj"
annotation["deprel"] = "amod"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)




##### ADVs #####
forms_to_annotate =  ["belki","bile","bugün","çok","en","En","diye","hemen","kesinlikle","sadece","sonra","yarın","acilen","ansızın","yokken","şimdi","beraber","birden","saatlerce","gerçekten","Ansızın","ansızın","neredeyse","yazın","birlikte","Günlerdir","günlerdir","artık","yeterince","kesinlikle","daha","Gece","gece"]
annotation = default_fields.copy()
annotation["upos"] = "ADV"
annotation["deprel"] = "advmod"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)













##############################################################################################################
##############################################################################################################

##### DETs #####
forms_to_annotate =  ["bir", "Bir"]
annotation = default_fields.copy()
annotation["upos"] = "DET"
annotation["xpos"] = "Indef"
annotation["deprel"] = "det"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)


##### QUES Part #####
forms_to_annotate =  ["mi", "mı", "mu", "mü"]
annotation = default_fields.copy()
annotation["upos"] = "AUX"
annotation["xpos"] = "Ques"
annotation["deprel"] = "discourse:q"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

##### VAR #####
forms_to_annotate =  ["var", "Var"]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["xpos"] = "Exist"
annotation["feats"] = "Number=Sing|Person=3|Polarity=Pos"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["vardı", "Vardı"]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["xpos"] = "Exist"
annotation["feats"] = "Evident=Fh|Number=Sing|Person=3|Polarity=Pos|Tense=Past"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["varmış", "Varmış"]
annotation = default_fields.copy()
annotation["upos"] = "NOUN"
annotation["xpos"] = "Exist"
annotation["feats"] = "Evident=Nfh|Number=Sing|Person=3|Polarity=Pos|Tense=Past"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

##### VERBs #####
#Pres
forms_to_annotate =  ["düşünüyor","düşünyor","ediyor","söylüyor","istiyor","planlıyor","sanıyor",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["feats"] = "Aspect=Imp|Number=Sing|Person=3|Polarity=Pos|Tense=Pres"
annotation["head"] = "0"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["istiyorum",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["feats"] = "Aspect=Imp|Number=Sing|Person=1|Polarity=Pos|Tense=Pres"
annotation["head"] = "0"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["ediliyor",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["feats"] = "Aspect=Imp|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|Voice=Pass"
annotation["head"] = "0"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Past
forms_to_annotate =  ["düşündü", "istedi"]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["feats"] = "Aspect=Perf|Evident=Fh|Number=Sing|Person=3|Polarity=Pos|Tense=Past"
annotation["head"] = "0"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["önerdim",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["feats"] = "Aspect=Perf|Evident=Fh|Number=Sing|Person=1|Polarity=Pos|Tense=Past"
annotation["head"] = "0"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["inanmış",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["feats"] = "Evident=Nfh|Number=Sing|Person=3|Polarity=Pos|Tense=Past"
annotation["head"] = "0"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["sorgulamamış",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["feats"] = "Evident=Nfh|Number=Sing|Person=3|Polarity=Neg|Tense=Past"
annotation["head"] = "0"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Hab
forms_to_annotate =  ["acıkır", "öğrenir", "olur", "uğrar", "ister"]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["feats"] = "Aspect=Hab|Number=Sing|Person=3|Polarity=Pos|Tense=Pres"
annotation["head"] = "0"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["ulaşamaz",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["feats"] = "Aspect=Hab|Mood=Pot|Number=Sing|Person=3|Polarity=Neg|Tense=Pres"
annotation["head"] = "0"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["yapabilir",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["feats"] = "Aspect=Hab|Mood=Pot|Number=Sing|Person=3|Polarity=Pos|Tense=Pres"
annotation["head"] = "0"
annotation["deprel"] = "root"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Ptcp yacak
forms_to_annotate =  ["acıkacağı","Alacağı","alacağı","ayrılacağı","atacağı","bahsedeceği","çalışacağı","çıkacağı","değiştireceği","evleneceği","gideceği","giyeceği","göndereceği","göreceği","içeceği","istediği","Konuşacağı","koparacağı","kesecek","okuyacağı","yiyeceği","yaşayacağı","olacak","olacağı","oturacağı","ödeyebileceği","süpüreceği","yapacağı","öğreneceği","öpeceği","sahipleneceği","uğrayacağı","sileceği",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Prosp|Polarity=Pos|Tense=Fut|VerbForm=Part"
annotation["deprel"] = "acl"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["Gideceğim",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Prosp|Mood=Pot|Number=Sing|Person=1|Polarity=Pos"
annotation["deprel"] = "acl"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["keseceğine","olacağına",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Case=Dat|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3|Polarity=Pos"
annotation["deprel"] = "acl"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["bahsedeceğini","çözebileceğini","kanıtlayacağını","olacağını",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Case=Acc|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3|Polarity=Pos"
annotation["deprel"] = "acl"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["okuyabileceği",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Prosp|Mood=Pot|Polarity=Pos|Tense=Fut|VerbForm=Part"
annotation["deprel"] = "acl"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["ulaşamayacağı",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Prosp|Mood=Pot|Polarity=Neg|Tense=Fut|VerbForm=Part"
annotation["deprel"] = "acl"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["getirmeyeceğinden",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Prosp|Case=Abl|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3|Polarity=Neg|Tense=Fut|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["getirmeyeceklerinden",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Prosp|Case=Abl|Number=Sing|Number[psor]=Plur|Person=3|Person[psor]=3|Polarity=Neg|Tense=Fut|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Ptcp dık
forms_to_annotate =  ["arzuladığı","çalıştığı","düşündüğü","ettiği","yaptığı","planladığı","sandığı","söylediği","anlaştığı","olduğu","okuduğu","Okuduğu",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Perf|Case=Nom|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3|Polarity=Pos|Tense=Past|VerbForm=Part"
annotation["deprel"] = "acl"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["istediğim", "önerdiğim"]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Perf|Case=Nom|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=1|Polarity=Pos|Tense=Past|VerbForm=Part"
annotation["deprel"] = "acl"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["gerektiğini","hoşlandığını","yaptığını","olduğunu","pişirildiğini","girdiğini",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Perf|Case=Acc|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3|Polarity=Pos|Tense=Past|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["olmadığını",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Perf|Case=Acc|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3|Polarity=Neg|Tense=Past|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["yaptığın",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Perf|Number[psor]=Sing|Person[psor]=2|Polarity=Pos|Tense=Past|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["yaptığına",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Perf|Case=Dat|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3|Polarity=Pos|Tense=Past|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["olduğundan",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Perf|Case=Abl|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3|Polarity=Pos|Tense=Past|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["biriktirdikten"]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Aspect=Perf|Case=Abl|Number=Sing|Person=3|Polarity=Pos|Tense=Past|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Ptcp An
forms_to_annotate =  ["olan","benzeyen","gelen","gören","isteyen",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Polarity=Pos|Tense=Pres|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["olmayan",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Polarity=Neg|Tense=Pres|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["olanın","girenin",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Case=Gen|Polarity=Pos|Tense=Pres|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["olanlardan",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Case=Gen|Number=Plur|Polarity=Pos|Tense=Pres|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["pişirilen","geçilen","edilen","konuşulan",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Number=Sing|Polarity=Pos|Tense=Pres|VerbForm=Part|Voice=Pass"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["çözebilen"]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Ptcp"
annotation["feats"] = "Mood=Pot|Number=Sing|Polarity=Pos|Tense=Pres|VerbForm=Part"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Conv
forms_to_annotate =  ["çalışırken", "gelirken"]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Conv"
annotation["feats"] = "Polarity=Pos|VerbForm=Conv"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["uyumadan",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Conv"
annotation["feats"] = "Case=Abl|Number=Sing|Person=3|Polarity=Pos|VerbForm=Conv"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["getirip", "bırakıp", "çıkınca", "kazanınca"]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Conv"
annotation["feats"] = "Polarity=Pos|VerbForm=Conv"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

#Vnoun
forms_to_annotate =  ["almayı","çalışmayı","etmeyi","geçmeyi",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Vnoun"
annotation["feats"] = "Case=Acc|Number=Sing|Person=3|Polarity=Pos|VerbForm=Vnoun"
annotation["deprel"] = "ccomp"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["açmak","almak","avlamak","ayrılmak","bahsetmek","bakmak","Bakmak","atmak","bastırmak","binmek","bırakmak","bulunmak","çalışmak","çizmek","çıkmak","değiştirmek","dikmek","dinlemek","dinlenmek","Dinlenmek","dövüşmek","edinmek","etmek","öpmek","sahiplenmek","Silmek","silmek","sökmeyi","süpürmek","taşınmak","uğramak","uyumak","yakalamak","yazmak","yapmak","yaşamak","evlenmek","ezberlemek","girmek","gitmek","Gitmek","giymek","görmek","görüşmek","götürmek","içmek","işletmek","kırmak","kiralamak","konuşmak","koparmak","keşfetmek","okumak","oturmak","olmak","beslemek","koymak","asmak","tamamlamak","danışmak","sulamak","tutmak","izlemek","vermek","toplamak",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Vnoun"
annotation["feats"] = "Case=Nom|Number=Sing|Person=3|Polarity=Pos|VerbForm=Vnoun"
annotation["deprel"] = "ccomp"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["yürütmek",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Vnoun"
annotation["feats"] = "Case=Nom|Number=Sing|Person=3|Polarity=Pos|VerbForm=Vnoun|Voice=Cau"
annotation["deprel"] = "ccomp"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["almasının",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Vnoun"
annotation["feats"] = "Case=Gen|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3|Polarity=Pos|VerbForm=Vnoun"
annotation["deprel"] = "ccomp"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["belirlemesi", "katılması",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Vnoun"
annotation["feats"] = "Case=Nom|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3|Polarity=Pos|VerbForm=Vnoun"
annotation["deprel"] = "ccomp"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["olmasını", "okumasını",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Vnoun"
annotation["feats"] = "Case=Acc|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=3|Polarity=Pos|VerbForm=Vnoun"
annotation["deprel"] = "ccomp"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

forms_to_annotate =  ["bakmamı",]
annotation = default_fields.copy()
annotation["upos"] = "VERB"
annotation["upos"] = "Vnoun"
annotation["feats"] = "Case=Acc|Number=Sing|Number[psor]=Sing|Person=3|Person[psor]=1|Polarity=Pos|VerbForm=Vnoun"
annotation["deprel"] = "ccomp"
annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)

