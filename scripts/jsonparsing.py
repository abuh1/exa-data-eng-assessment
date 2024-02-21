import os
import itertools
import sys
sys.path.append('Z:\\Documents\\projects\\exa-data-eng-assessment')
from src.pipeline.extract import extract_data

main_path = os.listdir('..\\data')
json_paths = ['..\\data\\' + p for p in main_path]

# create generator for json data
extracted = extract_data(json_paths)

# empty list will include all 'resourceType' from all the data
# unique_fields = []

# for resource in extracted:
#     if resource['resourceType'] not in unique_fields:
#         unique_fields.append(resource['resourceType'])
        
# uq = sorted(unique_fields)
# print(uq)
# print(f"\nLength of list: {len(uq)}")

data = next(extracted)

def testgen(d): 
    for entry in d['entry']:
        # Adding fullUrl as 'id' in 'patient' resource so it can be used as primary key in the database.
        # Also changing 'id' in resource to resource_id to clean up confusion.
        full_url = entry['fullUrl']
        resource = entry['resource']
        # replaces 'id' with 'resource_id' and adds full_url as 'id'
        try:
            resource['resource_id'] = resource.pop('id')
        except KeyError:
            print("Error: 'id' is undefined")
        resource['id'] = full_url
        yield resource
        
# chaining generator function to extend it
combined_gen = (testgen(d) for d in extracted)
big_gen = itertools.chain(*combined_gen)


# Recursive function to flatten nested dictionaries within a single json dictionary
def flatten_dict(data: dict, parent_key='', seperator='_'):
    """
        Flatten a dictionary with nested values.
    
        Args:
            data (dict): Nested dictionary to flatten
            parent_key: 
            seperator: seperating string for new flattened key
    """
    items = []
    for k, v in data.items():
        new_key = parent_key + seperator + k if parent_key else k
        if isinstance(v, dict):
            try:
                items.extend(flatten_dict(v, new_key, seperator=seperator).items())
            except RecursionError:
                print("Error: Recursion depth exceeded.")
                return None
        else:
            items.append((new_key, v))
    return dict(items)

one = next(big_gen)
print(one)