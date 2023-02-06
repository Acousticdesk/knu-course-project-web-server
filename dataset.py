import json

dataset = open('./real-estate.json')

real_estate = json.load(dataset)

print("Example: ", json.dumps(real_estate[0], indent=2, ensure_ascii=False))

dataset.flush()
dataset.close()
