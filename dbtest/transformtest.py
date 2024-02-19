import json
import psycopg2
import sys
sys.path.append('Z:\\Documents\\projects\\exa-data-eng-assessment')
from src.pipeline.extract import extract_data

data = ['data\\Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json']
extracted = extract_data(data)
patient = next(extracted)

def flatten_dict(d, parent_key='', sep='_'):
    """
    Flatten a dictionary with nested values.
    """
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

flattened_dict = flatten_dict(patient)
print(flattened_dict)