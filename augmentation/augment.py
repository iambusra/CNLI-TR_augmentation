from augmenter import create_augmented_version


TAGS_1 = ["PROPN"] #PROPN
TAGS_2 = ["NOUN", "ADV", "ADJ"] #NON-PROPN
TAGS_3 = ["PROPN", "NOUN", "ADV", "ADJ"] #ALL



create_augmented_version("split_1_annotated.conllu", "v1.conllu", TAGS_1)
create_augmented_version("split_1_annotated.conllu", "v2.conllu", TAGS_2)
create_augmented_version("split_1_annotated.conllu", "v3.conllu", TAGS_3)

create_augmented_version("v1.conllu", "v4.conllu", TAGS_2)
create_augmented_version("v1.conllu", "v5.conllu", TAGS_3)
create_augmented_version("v2.conllu", "v6.conllu", TAGS_1)
create_augmented_version("v2.conllu", "v7.conllu", TAGS_3)
create_augmented_version("v3.conllu", "v8.conllu", TAGS_1)
create_augmented_version("v3.conllu", "v9.conllu", TAGS_3)

"""
v0:

v1: v0 + change PROPN

v2: v0 + change NON-PROPN 

v3: v0 + change ALL       

v4: v1 + change NON-PROPN 

v5: v1 + change ALL 	  

v6: v2 + change PROPN 	  

v7: v2 + change ALL

v8: v3 + change PROPN

v9: v3 + change ALL

"""