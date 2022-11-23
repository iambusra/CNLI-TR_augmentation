import random

from file_handler import get_csv_data
from lemma_csv import csv_to_syn_dict

synonyms_file = ""
synonyms = dict()#csv_to_syn_dict(synonyms_file)

names_prev = dict()


def get_synonym(word):
	return word
	return synonyms[word]


def get_random_name(name):
	if name not in names_prev.keys():
		names_prev[name] = __randomize_name(name)

	return names_prev[name]

def __randomize_name(name):
	names = __get_name_list()

	random_name = random.choice(names)
	
	while (random_name == name):
		random_name = random.choice(names)

	return random_name

def __get_name_list():
	names = [item[0].split('\t')[1] for item in get_csv_data('name_data.csv')[1:]]
	names += [item[0].split('\t')[1] for item in get_csv_data('name_data2.csv')[2:]]

	return names


def flush_names():
	while(len(names_prev) != 0):
		names_prev.popitem()

def get_names():
	return names_prev

