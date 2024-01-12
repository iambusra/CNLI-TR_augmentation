import json
import stanza
from tqdm import tqdm

stanza.download('tr')

# Initialize the stanza pipeline for Turkish language
nlp = stanza.Pipeline(lang='tr', processors='tokenize,mwt,pos')


def morph_analysis(text):
    doc = nlp(text)
    
    analysis = []
    for sentence in doc.sentences:
        for i, token in enumerate(sentence.tokens):
            #lemma = token.words[0].lemma,
            text = token.text
            pos = token.words[0].upos
            features = token.words[0].feats
            if not features:
                features = ""
            #"token": ".".join([text, pos, features])

            analysis.append("|".join([text, pos, features]))

    return "\n".join(analysis)


def process_dataset(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        dataset = json.load(f)

    new_dataset = []
    progress_bar = tqdm(total=len(dataset), desc='Processing dataset', unit='data')

    for data in dataset:
        #premise_text = data['premise']
        #hypothesis_text = data['hypothesis']
        #premise_analysis = morph_analysis(premise_text)
        #hypothesis_analysis = morph_analysis(hypothesis_text)

        new_data = data
        new_data['premise'] = morph_analysis(data['premise'])
        new_data['hypothesis'] = morph_analysis(data['hypothesis'])

        new_dataset.append(new_data)

        progress_bar.update(1)

    progress_bar.close()

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(new_dataset, f, ensure_ascii=False, indent=2)


# Usage
input_file = 'data_dev.json'
output_file = 'new_data_dev.json'
process_dataset(input_file, output_file)

input_file = 'data_test.json'
output_file = 'new_data_test.json'
process_dataset(input_file, output_file)

input_file = 'data_train.json'
output_file = 'new_data_train.json'
process_dataset(input_file, output_file)
