import json
from collections import Counter

# path to one json file from the data directory
json_path = 'data\\Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json'

# extract json data
def extract_data(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        for entry in data['entry']:
            resource = entry['resource']
            yield resource

# select 'patient' entry of the file
resource = extract_data(json_path)

