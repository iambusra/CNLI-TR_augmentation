import json
import torch
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertForSequenceClassification, AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
from torch.optim import AdamW
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import pandas as pd
from collections import defaultdict


# Load dataset
def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Dataset class
class InferenceDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# Function to compute metrics
def compute_metrics(pred_labels, true_labels):
    precision, recall, _, _ = precision_recall_fscore_support(true_labels, pred_labels, average='binary')
    acc = accuracy_score(true_labels, pred_labels)
    return {
        'accuracy': acc,
        'precision': precision,
        'recall': recall
    }

# Model training function
def train(model, tokenizer, train_data, dev_data, device, class_weights):
    train_loader = DataLoader(train_data, batch_size=8, shuffle=True)
    dev_loader = DataLoader(dev_data, batch_size=8, shuffle=False)
    #train_loader = DataLoader(train_data, batch_size=8, shuffle=False)

    optimizer = AdamW(model.parameters(), lr=2e-5)

    # Use a weighted loss function to balance out the skewed dataset
    loss_fn = torch.nn.CrossEntropyLoss(weight=class_weights.to(device))

    for epoch in range(3):
        model.train()
        for batch in train_loader:
            optimizer.zero_grad()
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)

            # Compute loss using the logits and the labels
            loss = loss_fn(outputs.logits, labels)
            loss.backward()
            optimizer.step()

        model.eval()
        total_eval_accuracy = 0
        total_eval_precision = 0
        total_eval_recall = 0
        for batch in dev_loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)
            with torch.no_grad():
                outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs[0]
            predictions = torch.argmax(logits, dim=-1).cpu().numpy()
            label_ids = labels.cpu().numpy()
            metrics = compute_metrics(predictions, label_ids)
            total_eval_accuracy += metrics['accuracy']
            total_eval_precision += metrics['precision']
            total_eval_recall += metrics['recall']

        avg_accuracy = total_eval_accuracy / len(dev_loader)
        avg_precision = total_eval_precision / len(dev_loader)
        avg_recall = total_eval_recall / len(dev_loader)

        print(f"Epoch {epoch + 1}: Accuracy: {avg_accuracy}, Precision: {avg_precision}, Recall: {avg_recall}")

    return avg_accuracy, avg_precision, avg_recall

# Model evaluating function
def evaluate(model, test_data, device):
    test_loader = DataLoader(test_data, batch_size=8, shuffle=False)
    model.eval()
    total_eval_accuracy = 0
    total_eval_precision = 0
    total_eval_recall = 0

    for batch in test_loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        with torch.no_grad():
            outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs[0]
        predictions = torch.argmax(logits, dim=-1).cpu().numpy()
        label_ids = labels.cpu().numpy()
        metrics = compute_metrics(predictions, label_ids)
        total_eval_accuracy += metrics['accuracy']
        total_eval_precision += metrics['precision']
        total_eval_recall += metrics['recall']

    avg_accuracy = total_eval_accuracy / len(test_loader)
    avg_precision = total_eval_precision / len(test_loader)
    avg_recall = total_eval_recall / len(test_loader)
    
    return avg_accuracy, avg_precision, avg_recall



# Main function
def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load data
    train_data = load_dataset('data_train.json')
    dev_data = load_dataset('data_dev.json')
    test_data = load_dataset('data_test.json')

    # Class weights to handle imbalance
    class_weights = torch.tensor([0.85, 0.15]).to(device)

    # Model identifiers
    model_identifiers = [
    "emrecan/bert-base-multilingual-cased-allnli_tr",
    "emrecan/bert-base-turkish-cased-allnli_tr"
    ]
    results = []

    for model_identifier in model_identifiers:
        print(f"Training with {model_identifier}...")

        # Initialize tokenizer and model for each model identifier
        tokenizer = AutoTokenizer.from_pretrained(model_identifier)
        config = AutoConfig.from_pretrained(model_identifier, num_labels=2)  # Set to 2 for binary classification
        model = AutoModelForSequenceClassification.from_pretrained(
            model_identifier, 
            config=config, 
            ignore_mismatched_sizes=True  # Ignore size mismatch in the final layer
        )
        model.to(device)

        # Tokenize the data
        def tokenize_data(data, tokenizer):
            sentences1 = [item['sentence1'] for item in data]
            sentences2 = [item['sentence2'] for item in data]
            labels = [item['gold_label'] for item in data]
            encodings = tokenizer(sentences1, sentences2, truncation=True, padding=True, max_length=128)
            return InferenceDataset(encodings, labels)

        # Prepare the datasets
        train_dataset = tokenize_data(train_data, tokenizer)
        dev_dataset = tokenize_data(dev_data, tokenizer)
        test_dataset = tokenize_data(test_data, tokenizer)

        # Train the model
        acc, precision, recall = train(model, tokenizer, train_dataset, dev_dataset, device, class_weights)

        # Evaluate the model on the test dataset
        test_acc, test_precision, test_recall = evaluate(model, test_dataset, device)

        # Append results for both training and testing
        results.append({
            'model': model_identifier,
            'train_accuracy': acc,
            'train_precision': precision,
            'train_recall': recall,
            'test_accuracy': test_acc,
            'test_precision': test_precision,
            'test_recall': test_recall
        })

        # Save each trained model
        model_save_path = f"trained_{model_identifier.replace('/', '_')}.pt"
        torch.save(model.state_dict(), model_save_path)
        print(f"Model saved to {model_save_path}")

    # Save results to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv('nli_experiment_results.csv', index=False)

    print("Experiments completed. Results saved to nli_experiment_results.csv")

if __name__ == "__main__":
    main()

