import re
from file_handler import read_file, write_to_file

fields = {"id": 0, "form": 1, "lemma": 2, "upos": 3, "xpos": 4,
           "feats": 5, "head": 6, "deprel": 7, "deps": 8, "misc": 9}

# This program assumes that conllu file doesn't contain words with the character '\t' (tab)

def annotate_in_bulk(base_file, new_file, forms, annotation_data):
    conllu_lines = read_file(base_file)

    for form in forms:
        conllu_lines = annotate(form, annotation_data, conllu_lines)

    data = "".join(conllu_lines)

    write_to_file(new_file, data)



def annotate(form, annotation_data, conllu_lines):
    for i in range(len(conllu_lines)):
        line = conllu_lines[i]

        if(line[0].isnumeric() and get_form(line) == form):
            line = edit_line(line, annotation_data)
            conllu_lines[i] = line

    return conllu_lines



def get_form(line):
    return re.findall("\t.*\t", line)[0].split('\t')[1]



def edit_line(line, annotation_data):
    field_no = 0
    for key in annotation_data.keys():
        if annotation_data[key] is not None:
            line = put_data_to(line, annotation_data[key], field_no)
        
        field_no += 1

    return line



def put_data_to(line, data, field_no):
    tab_pos = get_tab_positions(line)

    end = tab_pos[field_no] if field_no < 9 else len(line)-1
    start = tab_pos[field_no-1]+1 if field_no > 0 else 0

    return line[:start]+data+line[end:]



def get_fields(line):
    fields = {"id": None, "form": None, "lemma": None, "upos": None, "xpos": None,
           "feats": None, "head": None, "deprel": None, "deps": None, "misc": None}

    tab_pos = get_tab_positions(line)

    key_num = 0
    for key in fields:
        if key_num != 0:
            start = tab_pos[key_num-1]+1
        else:
            start = None

        if key_num != 9:
            end = tab_pos[key_num]
        else:
            end = len(line)-1

        fields[key] = line[start:end]

        key_num += 1

    return fields



def get_tab_positions(text):
    return [s.start() for s in re.finditer('\t', text)]


