# -*- coding: utf-8 -*-

import datetime

import torch
import transformers
from datasets import load_dataset

class NLITRReader(torch.utils.data.Dataset):
  def __init__(self, dataset_name, split_name, max_example_num=-1):
    data_files_all = {"train": "data/data_train.json", "test": "data/data_test.json", "validation": "data/data_dev.json"}
    self.dataset = load_dataset('json', data_files=data_files_all)# data_files='data_train.json' #('nli_tr', dataset_name) 
    self.split_name = split_name
    self.max_example_num = max_example_num


  def read(self):
      count = 0
      for example in self.dataset[self.split_name]:
          if example['gold_label'] == -1: # skip examples having no gold value.
              continue
          count += 1
          if self.max_example_num > 0 and count >= self.max_example_num:
             break
          yield example


import torch
class NLITRDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

"""## Trainer"""

import torch
import pandas as pd
from transformers import TrainingArguments, Trainer, AutoConfig, AutoTokenizer, AutoModelForSequenceClassification

from sklearn.metrics import accuracy_score, precision_recall_fscore_support, precision_score, recall_score, confusion_matrix


def compute_metrics(pred):
    labels = pred.label_ids

    print("##################################    labels   #################################################")
    print(labels)
    print("################################################################################################")
    
    preds = pred.predictions.argmax(-1)
    
    print("################################## predictions #################################################")
    print(preds)
    print("################################################################################################")

    precision = precision_score(y_true=labels, y_pred=preds)
    print("precision score: ", precision)

    recall = recall_score(y_true=labels, y_pred=preds)
    print("recall score: ", recall)

    c_matrix = confusion_matrix(y_true=labels, y_pred=preds, labels=[0, 1])
    print("confusion matrix: \n", c_matrix)

    acc = accuracy_score(labels, preds)
    return {
        'accuracy': acc,
    }

from torch import nn
from torch.nn import functional as F

class CustomTrainer(Trainer):
    def compute_loss(self, model, inputs, return_outputs=False):
        labels = inputs.get("labels")

        # forward pass
        outputs = model(**inputs)
        logits = outputs.get("logits")

        #loss1 = F.cross_entropy(labels, logits.view(-1, 2), weight=torch.tensor([18.0, 89.0]))

        loss_fct = nn.CrossEntropyLoss(weight=torch.tensor([18.0, 89.0])) # change this
        loss = loss_fct(logits.view(-1, self.model.config.num_labels), labels.view(-1))

        return (loss, outputs) if return_outputs else loss


MAX_TRAIN_EXAMPLE_NUM = -1
MAX_EVALUATION_EXAMPLE_NUM = -1
class NLITRTrainer():
    def __init__(self, 
                 model_name='bert-base-cased', 
                 dataset_name='data', ###
                 evaluation_split='validation',
                 num_labels=2,##num_labels=2 
                 hypothesis_only=False):
        self.model_name = model_name
        self.dataset_name = dataset_name
        self.evaluation_split = evaluation_split
        self.hypothesis_only = hypothesis_only
        self.max_train_example_num = MAX_TRAIN_EXAMPLE_NUM
        self.max_evaluation_example_num = MAX_EVALUATION_EXAMPLE_NUM

        print('You can set the values of the following parameters via the global variables MAX_TRAIN_EXAMPLE_NUM and MAX_EVALUATION_EXAMPLE_NUM (-1 to use all examples in the splits)')
        print('max_train_example_num',self.max_train_example_num)
        print('max_evaluation_example_num',self.max_evaluation_example_num)
        self.prepare_for_training()
    
    def prepare_for_training(self):
        self.prepare_model()
        self.prepare_datasets()
        self.prepare_trainer()

    def prepare_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.config = AutoConfig.from_pretrained(self.model_name, num_labels=2)#num_labels=3
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, config=self.config)
        

    def get_dataset(self, split_name, max_example_num):
        df = pd.DataFrame(list(NLITRReader(dataset_name=self.dataset_name, split_name=split_name, max_example_num=max_example_num).read()))
        #df = self.get_weighted_read(df)

        labels = df['gold_label'].values.tolist()

        num_entailment = [element for element in labels if element == 1]
        print("TOTAL ENTAILMENT:", len(num_entailment))
        
        num_neutral = [element for element in labels if element == 0]
        print("TOTAL NEUTRAL:", len(num_neutral))

        if(split_name != 'train'):
            print(split_name, "split dere-dedicto labels:")
            print(df['d_r'].values.tolist())

        premises = df['premise'].values.tolist()

        if self.hypothesis_only:
            inputs = self.tokenizer(premises, truncation=True, padding=True)
        else:
            hypotheses = df['hypothesis'].values.tolist()
            inputs = self.tokenizer(premises, hypotheses, truncation=True, padding=True)
        
        dataset = NLITRDataset(inputs, labels)
        return dataset

    #-------------------
    """
    def get_ambiguous_dataset(self, split_name, max_example_num):
        df = pd.DataFrame(list(NLITRReader(dataset_name=self.dataset_name, split_name=split_name, max_example_num=max_example_num).read()))
        dere_data = df.loc[df['d_r'] == "r"]
        dedicto_data = df.loc[df['d_r'] == "d"]

        ambiguous_data = df.loc[df['d_r'] == "d"]
    """


    def get_dere_dataset(self, split_name, max_example_num):
        df = pd.DataFrame(list(NLITRReader(dataset_name=self.dataset_name, split_name=split_name, max_example_num=max_example_num).read()))
        df = df.loc[df['d_r'] == "r"]

        labels = df['gold_label'].values.tolist() 
        premises = df['premise'].values.tolist()

        if self.hypothesis_only:
            inputs = self.tokenizer(premises, truncation=True, padding=True)
        else:
            hypotheses = df['hypothesis'].values.tolist()
            inputs = self.tokenizer(premises, hypotheses, truncation=True, padding=True)
        
        dataset = NLITRDataset(inputs, labels)
        return dataset


    def get_dedicto_dataset(self, split_name, max_example_num):
        df = pd.DataFrame(list(NLITRReader(dataset_name=self.dataset_name, split_name=split_name, max_example_num=max_example_num).read()))
        print("base dataset----->", df)
        df = df.loc[df['d_r'] == "d"]
        print("dedicto dataset----->", df)

        labels = df['gold_label'].values.tolist() #######
        premises = df['premise'].values.tolist() ######

        if self.hypothesis_only:
            inputs = self.tokenizer(premises, truncation=True, padding=True)
        else:
            hypotheses = df['hypothesis'].values.tolist()
            inputs = self.tokenizer(premises, hypotheses, truncation=True, padding=True)
        
        dataset = NLITRDataset(inputs, labels)
        return dataset


    def get_weighted_read(self, read):
        neutral_data = read.loc[read['gold_label'] == 0]
        neutral_ids = neutral_data['premise_id'].values.tolist()

        w_ids = [item for item in read.values if item[0] in neutral_ids]
        weighted_read = pd.DataFrame(w_ids, columns=['premise_id', 'premise', 'hypothesis_id', 'hypothesis', 'gold_label', 'd_r'])
        print(weighted_read)
        #weighted_read = read.loc[read['premise_id'] in neutral_ids]

        while( len([label for label in weighted_read['gold_label'].values.tolist() if label == 1]) < len(neutral_data) ):
            pair = read.sample()
            if(pair.values[0][0] not in weighted_read['premise_id'].tolist()):
                weighted_read = pd.concat([weighted_read, pair])

        print("WEIGHTED ENTAILMENT:", len([label for label in weighted_read['gold_label'].values.tolist() if label == 1]))
        print("WEIGHTED NEUTRAL:", len([label for label in weighted_read['gold_label'].values.tolist() if label == 0]))
        
        return weighted_read


    #--------------------------

    def prepare_datasets(self):
        self.train_dataset = self.get_dataset('train', max_example_num=self.max_train_example_num)
        self.evaluation_dataset = self.get_dataset(self.evaluation_split, max_example_num=self.max_evaluation_example_num)
      
    def prepare_trainer(self):
        training_args = TrainingArguments(
            output_dir='./results',          # output directory
            num_train_epochs=1,              # total number of training epochs
            per_device_train_batch_size=4,   # batch size per device during training444
            per_device_eval_batch_size=4,   # batch size for evaluation444
            gradient_accumulation_steps=32,  # gradient accumulation steps to increase effective batch size on GPU. 32
            warmup_steps=100,                # number of warmup steps for learning rate scheduler
            weight_decay=0.01,               # strength of weight decay
            logging_dir='./logs',            # directory for storing logs
            logging_steps=10
        )

        self.trainer = CustomTrainer(
            model=self.model,                         # the instantiated 🤗 Transformers model to be trained
            args=training_args,                       # training arguments, defined above
            train_dataset=self.train_dataset,         # training dataset
            eval_dataset=self.evaluation_dataset,     # evaluation dataset,
            compute_metrics=compute_metrics
        )

    def train(self):
        train_results = self.trainer.train()
        return train_results

    def evaluate(self):
        eval_results = self.trainer.evaluate()
        return eval_results

    #--------------------------

    def set_evaluation_split(self, split):
        print("split is:", split)
        self.evaluation_split = split
        self.evaluation_dataset = self.get_dataset(split, max_example_num=self.max_evaluation_example_num)
        self.trainer.eval_dataset = self.evaluation_dataset

        print("evaluation_split is:", self.evaluation_split)
        print("trainer_ds is :", self.trainer.eval_dataset)

    def evaluate_dere(self):
        dere_dataset = self.get_dere_dataset(self.evaluation_split, max_example_num=self.max_evaluation_example_num)
        self.trainer.eval_dataset = dere_dataset

        print("##################################     DERE    #################################################")
        print(self.evaluate())
        print("################################################################################################")
        print("")
        
        #self.evaluation_dataset = self.get_dataset(self.evaluation_split, max_example_num=self.max_evaluation_example_num)
        self.trainer.eval_dataset = self.evaluation_dataset


    def evaluate_dedicto(self):
        dedicto_dataset = self.get_dedicto_dataset(self.evaluation_split, max_example_num=self.max_evaluation_example_num)
        self.trainer.eval_dataset = dedicto_dataset
        
        print("##################################    DEDICTO   #################################################")
        print(self.evaluate())
        print("################################################################################################")
        print("")
        
        #self.evaluation_dataset = self.get_dataset(self.evaluation_split, max_example_num=self.max_evaluation_example_num)
        self.trainer.eval_dataset = self.evaluation_dataset


    def get_test_evaluation(self):
        test_dataset = self.get_dataset('test', max_example_num=self.max_evaluation_example_num)
        self.trainer.eval_dataset = test_dataset

        print("##################################    TEST   #################################################")
        test_eval = self.trainer.evaluate()
        print(test_eval)
        print("################################################################################################")
        print("")

        self.trainer.eval_dataset = self.evaluation_dataset
        return test_eval

    #--------------------------


"""## Experiment Manager

This is a simple experiment manager that runs a series of experiments with the given set of hyperparameters and returns the resulting metrics.
"""

import copy
import numpy as np
import random

class NLIExperiment:
    def __init__(self, experiment_parameters, seed=1234):
        self.experiment_parameters = experiment_parameters
        self.set_random_seed(seed)
    
    def set_random_seed(self, seed):
        np.random.seed(seed)
        random.seed(seed)
        torch.manual_seed(seed)
    
    def run(self):
        experiment_results = []
        
        for model_name in self.experiment_parameters['model_names']:
            experiment_parameters = {}
            experiment_parameters['model_name'] = model_name

            for dataset_name, evaluation_split_names in self.experiment_parameters['dataset_info'].items():
                experiment_parameters['dataset_name'] = dataset_name
            
                for evaluation_split_name in evaluation_split_names: #unimportant
                    experiment_parameters['evaluation_split_name'] = evaluation_split_name

                    for param_key, param_values in self.experiment_parameters['params'].items():
                        for param_value in param_values:
                            experiment_parameters[param_key] = param_value
                            print('\n\nA new experiment started...')
                            nlitr_trainer = NLITRTrainer(model_name=model_name, dataset_name=dataset_name, evaluation_split=evaluation_split_name, **{param_key:param_value})

                            print('Training...')
                            train_results = nlitr_trainer.train()

                            print('Evaluating...')
                            eval_results = nlitr_trainer.evaluate()#evaluate()
                             
                            experiment_parameters.update(eval_results)
                            print('\nexperiment parameters:', experiment_parameters)
                            print('experiment results:', eval_results)

                            experiment_results.append(copy.deepcopy(experiment_parameters))
                            #--------------------------
                            nlitr_trainer.evaluate_dere()
                            nlitr_trainer.evaluate_dedicto()

                            # comment out down below if it doesnt work

                            eval_results_test = nlitr_trainer.get_test_evaluation()
                            
                            """
                            nlitr_trainer.set_evaluation_split('test')
                            eval_results_test = nlitr_trainer.evaluate()
                            nlitr_trainer.set_evaluation_split('validation')
                            """

                            print('test split eval:', eval_results_test)

                            experiment_parameters.update(eval_results_test)
                            experiment_results.append(copy.deepcopy(experiment_parameters))
                            
                            #--------------------------
                            
                            

        return experiment_results

## Experiments

experiment_parameters0 = {
     'model_names' : ['dbmdz/bert-base-turkish-cased'], #alternative values: 'model_names' : ['bert-base-cased', 'bert-base-multilingual-cased', 'dbmdz/bert-base-turkish-cased'] 
     'dataset_info' : {'snli_tr': ['validation'], 'multinli_tr': ['validation_matched']},   #alternative values: {'snli_tr': ['validation', 'test'], 'multinli_tr': ['validation_matched', 'validation_mismatched']}
     'params' : {'hypothesis_only': [True, False]}
}


experiment_parameters = {
     'model_names' : ['dbmdz/bert-base-turkish-cased', 'bert-base-cased', 'bert-base-multilingual-cased'],  
     'dataset_info' : {'data': ['validation']}, #['test', 'validation']   #alternative values: {'snli_tr': ['validation', 'test'], 'multinli_tr': ['validation_matched', 'validation_mismatched']}
     'params' : {'hypothesis_only': [False]} # 'hypothesis_only': [True, False]
}

# 'model_names' : ['bert-base-multilingual-cased']
# 'dataset_info' : {'data_train.json': ['train'], 'data_test.json': ['test'], 'data_dev.json':['validation']}, 


# #You may set different values for the size of training and evaluation splits for fast iterations (-1 to use all examples in the splits). 
# MAX_TRAIN_EXAMPLE_NUM = 2048
# MAX_EVALUATION_EXAMPLE_NUM = 512

start = datetime.datetime.now()

experiment = NLIExperiment(experiment_parameters)
experiment_result = experiment.run()


experiment_result_df = pd.DataFrame(experiment_result)
experiment_result_df.head(n=100) #show all dataframe


print(experiment_result_df.head(n=100))

print("total elapsed time:", datetime.datetime.now() - start)

experiment_result_df.to_csv("experiment_results.csv")

