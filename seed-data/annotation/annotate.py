from annotator import annotate_in_bulk




default_fields = {"id": None, "form": None, "lemma": None, "upos": None, "xpos": None,
           "feats": None, "head": None, "deprel": None, "deps": None, "misc": None}




forms_to_annotate =  ["Naz","Fatma","Ahmet","Nazen","Utku","Rüstem","Ayşe","Mercan","Çağla","Hilmican","Meltem","Rumet","Yeter","Jüri","Fazıl","Yücel","Hüsnü","Nisa","Büşra","Kenan","Ufuk","Kaan","Saygın","Nihat","masaya","Turan","Zebercet","Leyla","Tevfik","Hande","Gamze","Tuna","Akif","Mehmet","Efe","Erçin","Hale","Hakan","Filiz","Serdar","Ozan","Ulrika","Fatih","Emilia","Azra","Nazlı","Miray","Ünzile","Şeyda","Yağız","Şükran","Banu","Deniz","Burak","Oğuz","Nazenin","Henrik","Çiğdem","Derin","Tijen","Jülide","Mahir","Can","Canan","Aybala","Irmak","Cemre","Rezzak","Ceyda","Yıldız","Fikri","Buğra","Ayten","Zahide","Nermin","Tülay"]
annotation = default_fields
annotation["upos"] = "PROPN"
annotation["feats"] = "Case=Nom|Number=Sing|Person=3"


annotate_in_bulk("new.conllu", "new.conllu", forms_to_annotate, annotation)


