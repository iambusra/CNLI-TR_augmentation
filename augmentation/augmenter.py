import re
import random
from types import MappingProxyType

from annotator import edit_line, get_fields
from file_handler import read_file, write_to_file, get_csv_data
from word_changer import get_random_name, get_synonym, flush_names


additives = MappingProxyType( 
	{
	'a': {'Nom': "", 'Acc': "ı", 'Dat': "a", 'Loc': "da", 'Abl': "dan", 'nst': "la", 'Gen': "ın"},
	'ı': {'Nom': "", 'Acc': "ı", 'Dat': "a", 'Loc': "da", 'Abl': "dan", 'nst': "la", 'Gen': "ın"},
	'o': {'Nom': "", 'Acc': "u", 'Dat': "a", 'Loc': "da", 'Abl': "dan", 'nst': "la", 'Gen': "un"},
	'u': {'Nom': "", 'Acc': "u", 'Dat': "a", 'Loc': "da", 'Abl': "dan", 'nst': "la", 'Gen': "un"},
	'e': {'Nom': "", 'Acc': "i", 'Dat': "e", 'Loc': "de", 'Abl': "den", 'nst': "le", 'Gen': "in"},
	'i': {'Nom': "", 'Acc': "i", 'Dat': "e", 'Loc': "de", 'Abl': "den", 'nst': "le", 'Gen': "in"},
	'ö': {'Nom': "", 'Acc': "ü", 'Dat': "e", 'Loc': "de", 'Abl': "den", 'nst': "le", 'Gen': "ün"},
	'ü': {'Nom': "", 'Acc': "ü", 'Dat': "e", 'Loc': "de", 'Abl': "den", 'nst': "le", 'Gen': "ün"}
	}
)

kaynastirma = MappingProxyType( 
	{
	'Nom': "", 
	'Acc': "y", 
	'Dat': "y", 
	'Loc': "", 
	'Abl': "", 
	'nst': "y", 
	'Gen': "n"
	}
)

vowels = "AIOUEİÖÜaıoueiöü"

def create_augmented_version(base_file, new_file, upos_tags):
	conllu_lines = read_file(base_file).copy()
	conllu_lines = augment_by(upos_tags, conllu_lines).copy()

	flush_names()

	data = "".join(conllu_lines)
	write_to_file(new_file, data)


def augment_by(upos_tags, conllu_lines):
	for i, line in enumerate(conllu_lines):
		if(line[0].isnumeric()):
			fields = get_fields(line).copy()

			augmented_fields = augment_data(fields, upos_tags)

			conllu_lines[i] = edit_line(conllu_lines[i], augmented_fields)

			text_index = i - int(line[0])
			conllu_lines[text_index] = conllu_lines[text_index].replace(fields['form'], augmented_fields['form'])

	return conllu_lines

"""
def check_tags(upos_tags, fields):
	is_propn, change = (fields['upos']=="PROPN"), (fields['misc']=="change=yes")
	
	if is_propn:
		return True

	for tag in upos_tags:
		if fields['upos'] == tag and change:
			return True
"""


def augment_data(fields, upos_tags):
	augmented_fields = fields.copy()

	if fields['upos'] == "PROPN" and "PROPN" in upos_tags:
		random_name = get_random_name(augmented_fields['lemma'])

		augmented_fields['lemma'] = random_name.replace("â", "a")
		augmented_fields['form'] = get_augmented_form(augmented_fields['lemma'], augmented_fields['feats'], True)

	elif fields['upos'] == "NOUN" and ("NOUN" in upos_tags) and fields['misc'] == "change=yes":
		augmented_fields['lemma'] = get_synonym(augmented_fields['lemma'])
		augmented_fields['form'] = get_augmented_form(augmented_fields['lemma'], augmented_fields['feats'], False)

	elif (fields['upos'] == "ADJ" or fields['upos'] == "ADV") and ("ADV" in upos_tags or "ADJ" in upos_tags)  and fields['misc'] == "change=yes":
		augmented_fields['lemma'] = get_synonym(augmented_fields['lemma'])
		augmented_fields['form'] = augmented_fields['lemma']
	
	if fields['id'] == "1":
		augmented_fields['form'] = augmented_fields['form'][:1].upper()+augmented_fields['form'][1:]

	return augmented_fields


"""
def augment_data(fields, upos_tags):
	try: 
		augmented_fields = fields.copy()

		if fields['upos'] == "PROPN" and "PROPN" in upos_tags:
			augmented_fields['lemma'] = get_random_name(augmented_fields['lemma'])
			augmented_fields['form'] = get_augmented_form(augmented_fields['lemma'], augmented_fields['feats'], True)

		elif fields['upos'] == "NOUN" and ("NOUN" in upos_tags) and fields['misc'] == "change=yes":
			augmented_fields['lemma'] = get_synonym(augmented_fields['lemma'])
			augmented_fields['form'] = get_augmented_form(augmented_fields['lemma'], augmented_fields['feats'], False)

		elif (fields['upos'] == "ADJ" or fields['upos'] == "ADV") and ("ADV" in upos_tags or "ADJ" in upos_tags)  and fields['misc'] == "change=yes":
			augmented_fields['lemma'] = get_synonym(augmented_fields['lemma'])
			augmented_fields['form'] = augmented_fields['lemma']
	
		if fields['id'] == "1":
			augmented_fields['form'] = augmented_fields['form'][:1].upper()+augmented_fields['form'][1:]
	except:
		print(fields)

	return augmented_fields
"""



def get_augmented_form(lemma, feats, is_propn):
	augmented_form = lemma

	augmented_form += get_plur_additive(augmented_form, feats)

	augmented_form += get_pos_additive(augmented_form, feats) 

	case = feats.split('|')[0][-3:] 
	augmented_form += get_case_additive(augmented_form, case, is_propn, ('psor' in feats))

	return augmented_form


def get_plur_additive(base, feats):
	plur_additive = ""
	print(base)
	additive_vowel = additives[get_last_vowel(base).lower()]['Dat']

	if "Number=Plur" in feats:
		plur_additive += "l"+additive_vowel+"r"

	return plur_additive


def get_pos_additive(base, feats):
	pos_additive = ""
	additive_vowel = additives[get_last_vowel(base).lower()]['Acc']

	number, person = "", ""
	feat_list = feats.split('|')
	for feat in feat_list:
		if "Person[psor]=" in feat:
			person = feat[-1]
		elif "Number[psor]=" in feat:
			number = feat[-4:]

	if person == '3':
		if base[-1] in vowels:
			pos_additive += "s"+additive_vowel
		else:
			pos_additive += additive_vowel

	elif person == '1' or person == '2':
		if base[-1] not in vowels: #is consonant
			pos_additive += additive_vowel

		if person == '2':
			pos_additive += "n"
		elif person == '1':
			pos_additive += "m"

		if number == "Plur":
			pos_additive += additive_vowel+"z"

	return pos_additive


def get_case_additive(base, case, is_propn, is_pos): # re adjust for non-names
	last_vowel = get_last_vowel(base).lower()
	additive = additives[last_vowel][case]

	if(last_vowel == base[-1]):
		if(not is_pos):
			additive = kaynastirma[case] + additive
		else:
			additive = 'n' + additive

	if(case != "Nom" and is_propn):
		additive = "'" + additive

	return additive


def get_last_vowel(text):
	vowels = "AIOUEİÖÜaıoueiöü"
	for char in reversed(text):
		if char in vowels:
			return char

	return None 