import json
import random

# Load your JSON dataset with UTF-8 encoding
with open('merged_dataset.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Calculate the number of items for the 70% and 30% splits
total_items = len(data)
split_ratio = 0.7  # 70% for one JSON and 30% for the other
split_index = int(total_items * split_ratio)

# Shuffle the dataset randomly
random.shuffle(data)

# Split the dataset into two parts
json_1 = data[:split_index]
json_2 = data[split_index:]

# Save the two JSONs to separate files with UTF-8 encoding
with open('json_1.json', 'w', encoding='utf-8') as json1_file:
    json.dump(json_1, json1_file, ensure_ascii=False, indent=4)

with open('json_2.json', 'w', encoding='utf-8') as json2_file:
    json.dump(json_2, json2_file, ensure_ascii=False, indent=4)

print("Splitting complete.")
