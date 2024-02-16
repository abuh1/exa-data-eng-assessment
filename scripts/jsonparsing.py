import json
from collections import Counter

# path to one json file from the data directory
json_path = 'data\Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json'

# extract json data
with open(json_path, 'r') as f:
    data = json.load(f)
    entries = data['entry']

resource_types = (entry for entry in entries)
print(type(resource_types))
    
# element_count = Counter(resource_types)
# for element, count in element_count.items():
#     print(f"{element}: {count}")
    

    