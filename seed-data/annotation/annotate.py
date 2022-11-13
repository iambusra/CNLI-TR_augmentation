from annotator import annotate_in_bulk




default_fields = {"id": None, "form": None, "lemma": None, "upos": None, "xpos": None,
           "feats": None, "head": None, "deprel": None, "deps": None, "misc": None}




forms_to_annotate = ["bir"]
annotation = default_fields
annotation["upos"] = "DET"
annotation["xpos"] = "Def"
annotation["misc"] = "Hello"

annotate_in_bulk("part_5.conllu", "new.conllu", forms_to_annotate, annotation)


