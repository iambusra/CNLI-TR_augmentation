import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import zeyrek

# Load data from file
with open('data/data_train.json', 'r') as f:
	train_data = json.load(f)
with open('data/data_dev.json', 'r') as f:
	dev_data = json.load(f)
with open('data/data_test.json', 'r') as f:
	test_data = json.load(f)

train_data = train_data + dev_data
	
# Get input data sets
train_premises = [example['premise'] for example in train_data]
train_hypotheses = [example['hypothesis'] for example in train_data]
train_labels = [example['gold_label'] for example in train_data]

test_premises = [example['premise'] for example in test_data]
test_hypotheses = [example['hypothesis'] for example in test_data]
test_labels = [example['gold_label'] for example in test_data]

analyzer = zeyrek.MorphAnalyzer()
def turkish_lemmatizer(text):
	tokens = text.split()   

	lemmatized_tokens = []
	for token in tokens:
		lemmatized_token = None
		try:
			lemmas = analyzer.lemmatize(token)[0][1]
			if token in lemmas:
				lemmatized_token = token
			else:
				lemmatized_token = max(lemmas, key=len)
			#print("lemmas:", lemmas)
			#print("token:", lemmatized_token)
		except KeyboardInterrupt:
			exit()

		if lemmatized_token:
			lemmatized_tokens.append(lemmatized_token)
		else:
			lemmatized_tokens.append(token)

	#print("tokens are:", lemmatized_tokens)
	print("text:", text) 
	print("out:", ' '.join(lemmatized_tokens))
	return ' '.join(lemmatized_tokens)


def produce_data(tokenizer=None):
	vectorizer = CountVectorizer(tokenizer=tokenizer)
		
	vectorizer.fit(train_premises)
	vectorizer.fit(train_hypotheses)

	vectorizer.fit(test_premises)
	vectorizer.fit(test_hypotheses)

	train_X = np.concatenate(
		[vectorizer.transform(train_premises).toarray(),
		 vectorizer.transform(train_hypotheses).toarray()], axis=1)
	train_y = np.array(train_labels)

	test_X = np.concatenate(
		[vectorizer.transform(test_premises).toarray(),
		 vectorizer.transform(test_hypotheses).toarray()], axis=1)
	test_y = np.array(test_labels)

	return (train_X, train_y, test_X, test_y)


class Model:
	name = ""
	model = None

	def __init__(self, train_X, train_y, test_X, test_y):
		self.train_X = train_X
		self.train_y = train_y
		self.test_X = test_X
		self.test_y = test_y
		self.pred_y = None

	def predict(self):
		self.model.fit(self.train_X, self.train_y)
		self.pred_y = self.model.predict(self.test_X)

	def evaluate(self):
		print(f"RUNNING {self.name}")
		print("-"*30)

		accuracy = accuracy_score(self.test_y, self.pred_y)
		print("Accuracy Score:", accuracy)

		# Calculate precision and recall for label 1
		precision = precision_score(self.test_y, self.pred_y, pos_label=1)
		recall = recall_score(self.test_y, self.pred_y, pos_label=1)
		print("Label 1 (Entailment) - Precision: {:.2f}, Recall: {:.2f}".format(precision, recall))

		# Calculate precision and recall for label 0
		precision = precision_score(self.test_y, self.pred_y, pos_label=0)
		recall = recall_score(self.test_y, self.pred_y, pos_label=0)
		print("Label 0 (Contradiction or neutrality) - Precision: {:.2f}, Recall: {:.2f}".format(precision, recall))

		precision = precision_score(self.test_y, self.pred_y, average='weighted')
		recall = recall_score(self.test_y, self.pred_y, average='weighted')
		print("TOTAL - Precision: {:.2f}, Recall: {:.2f}".format(precision, recall))
		print()


class KNN(Model):
	def __init__(self, train_X, train_y, test_X, test_y, k=200):
		super().__init__(train_X, train_y, test_X, test_y)
		self.name = "KNN"
		self.model = KNeighborsClassifier(
			n_neighbors=k,
			weights='distance'
		)

class RF(Model):
	def __init__(
		self,
		train_X, 
		train_y, 
		test_X, 
		test_y, 
		n_estimators=100, 
		max_depth=None,
		random_state=42,
	):
		super().__init__(train_X, train_y, test_X, test_y)
		self.name = "RF"
		self.model = RandomForestClassifier(
			n_estimators=n_estimators, 
			max_depth=max_depth, 
			random_state=random_state,
			class_weight='balanced_subsample',
			min_samples_leaf=5
		)

if __name__ == "__main__":
	raw_data = produce_data()

	raw_knn = KNN(*raw_data)
	raw_knn.predict()
	raw_knn.evaluate()

	raw_rf = RF(*raw_data)
	raw_rf.predict()
	raw_rf.evaluate()

	lemmatized_data = produce_data(turkish_lemmatizer)

	print("####### BELOW ARE LEMMATIZED #######")
	lemmatized_knn = KNN(*lemmatized_data)
	lemmatized_knn.predict()
	lemmatized_knn.evaluate()

	lemmatized_rf = RF(*lemmatized_data)
	lemmatized_rf.predict()
	lemmatized_rf.evaluate()
