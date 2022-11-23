import csv
import pandas as pd
from annotator import get_fields
from file_handler import read_file, write_to_file, get_csv_data

conllu_file = "split_1_annotated.conllu"
out_file = "lemmas_change_yes.csv"


def lemmas_to_csv(conllu_file, csv_file):
	conllu_lines = read_file(conllu_file)

	lemmas = dict()
	for line in conllu_lines:
		if(line[0].isnumeric()):
			fields = get_fields(line)

			if fields['misc'] == "change=yes":
				lemmas[fields['lemma']] = ""

		convert_to_csv(lemmas.keys())


def convert_to_csv(data):
	df = pd.DataFrame(data)
	df.to_csv(out_file)


def csv_to_syn_dict(csv_file):
	csv_data = get_csv_data(out_file)[1:]
	
	synonyms = dict()

	for row in csv_data:
		synonyms[row[1]] = row[2]
		synonyms[row[2]] = row[3]

	return synonyms


"""
lemmas_to_csv(conllu_file, out_file)
csv_to_syn_dict(out_file)
"""