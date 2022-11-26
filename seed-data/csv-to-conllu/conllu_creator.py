import re 
import csv

csv_filename = "data.csv"
row_num = 360


punct_list = ["!", "?", ",", ";", ":", "-", "*", "."] #no . and '
annotation = "\t_\t_\t_\t_\t_\t_\t_\t_"


def get_csv_data():
	data = []
	with open(csv_filename, "r") as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		return [row for row in csv_reader][:row_num]	


def lemmatize(sentence):
	sentence = sentence.strip()
	for punct in punct_list:
		sentence = sentence.replace(punct, " "+punct+" ")

	return sentence.split()


def annotate(lemmas):
    return [str(i+1) + "\t" + lemmas[i] + annotation for i in range(len(lemmas))]


def convert_sentence(sentence):
	converted = ""

	lemmas = lemmatize(sentence)
	lemmas = annotate(lemmas)
	for lemma in lemmas:
		converted += lemma + "\n"

	return converted



def convert_to_connllu(data):
	connllu = ""
	for row in data:
		connllu += "# sent_id = " + row[0] + "\n"
		connllu += "# text = " + row[1] + "\n"
		connllu += convert_sentence(row[1]) + "\n"

	return connllu


# -----
data = get_csv_data()
conllu = convert_to_connllu(data[1:])

with open('out.conllu', 'w') as f:
    f.write(conllu)
