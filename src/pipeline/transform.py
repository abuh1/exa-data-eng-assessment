import itertools
from extract import extract_data

# Testing purposes
data = ['data\\Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json']
extracted = extract_data(data)

# Takes in resource generator and flattens and maps to SQL schema to discard any data that isn't in the schema.
def transform_data():
    pass

# Takes in generator yielded from extract function and reproduces a new generator with all 'resource' from all files.
def combine_all_resources():
    pass

def grab_resources(data):
    """
        Grabs every 'resource' from json data extracted from extract_data.
        
        Parameters:
            data (generator object): input extracted json generator object from extract module.
            
        Yields:
            resources (generator object): generator object containing all resources from the json extract.
    """
    for entry in data['entry']:
        # Adding fullUrl as 'id' in all resources so to use as primary key in the database.
        # Also changing previous 'id' in resources to resource_id.
        full_url = entry['fullUrl']
        resource = entry['resource']
        # replaces 'id' with 'resource_id' and adds full_url as 'id'
        try:
            resource['resource_id'] = resource.pop('id')
        except KeyError:
            print("Error: 'id' is undefined")
        resource['id'] = full_url
        yield resource
        
        
# Recursive function to flatten nested dictionaries within a single json dictionary
def flatten_dict(data, parent_key='', seperator='_'):
    """
    Flatten a dictionary with nested values.
    """
    items = []
    for k, v in data.items():
        new_key = parent_key + seperator + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=seperator).items())
        else:
            items.append((new_key, v))
    return dict(items)