import json

# Load the data from the three JSON files
with open('data_dev.json', 'r', encoding='utf-8') as dev_file:
    data_dev = json.load(dev_file)

with open('data_test.json', 'r', encoding='utf-8') as test_file:
    data_test = json.load(test_file)

with open('data_train.json', 'r', encoding='utf-8') as train_file:
    data_train = json.load(train_file)

# Merge the data from the three files into one dictionary
merged_data = {
    'dev': data_dev,
    'test': data_test,
    'train': data_train
}

# Save the merged data to a single JSON file
with open('merged_data.json', 'w', encoding='utf-8') as merged_file:
    json.dump(merged_data, merged_file, ensure_ascii=False, indent=4)

print("Merging complete.")
