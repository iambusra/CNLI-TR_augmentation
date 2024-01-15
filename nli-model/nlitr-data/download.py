from datasets import load_dataset
import json

# Load the dataset
dataset = load_dataset("nli_tr", "multinli_tr")

# Define the path for the merged JSON file
merged_json_file_path = "merged_dataset.json"

# Initialize an empty list to store all splits
all_splits = []

# Loop through all splits and convert them to a list of dictionaries
for split_name in dataset.keys():
    dataset_split = dataset[split_name]
    dataset_list = dataset_split.to_pandas().to_dict(orient="records")
    all_splits.extend(dataset_list)

# Write the merged dataset to the JSON file
with open(merged_json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(all_splits, json_file, ensure_ascii=False, indent=4)

print(f"Merged dataset has been saved to {merged_json_file_path}")
