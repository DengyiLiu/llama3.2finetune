import json
from datasets import load_dataset


dataset = load_dataset("databricks/databricks-dolly-15k")
transformed_data = []


for example in dataset['train']:
    instruction = example['instruction'].strip() if example['instruction'] else ""
    context = example['context'].strip() if example['context'] else ""
    response = example['response'].strip() if example['response'] else ""

    
    transformed_entry = {
        "instruction": instruction,
        "input": context,
        "output": response
    }

    transformed_data.append(transformed_entry)

# save as json
with open('dolly15k_transformed.json', 'w', encoding='utf-8') as f:
    json.dump(transformed_data, f, ensure_ascii=False, indent=4)

print("save as dolly15k_unsloth.jsonl")
