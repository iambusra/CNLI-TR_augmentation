import re
from file_handler import read_file, write_to_file, create_csv
from collections import defaultdict

def get_forms(filename):
	lines = read_file(filename)

	forms = defaultdict(int)
	lines = [line for line in lines if line[0].isnumeric()]
		
	for line in lines:
		form = re.findall("\t.*\t", line)[0].split('\t')[1]

		#UNUSED:
		if form in forms:
			forms[form] += 1
		else:
			forms[form] = 1
		#UNUSED

	return forms.keys()

forms = get_forms("split_1.conllu")

data = ",".join(forms)
create_csv(forms, "split_1.csv")

