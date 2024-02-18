import os
import sys
sys.path.append('Z:\\Documents\\projects\\exa-data-eng-assessment')
from src.pipeline.extract import extract_data

main_path = os.listdir('..\\data')
json_paths = ['..\\data\\' + p for p in main_path]

# create generator for json data
extracted = extract_data(json_paths)

# empty list will include all 'resourceType' from all the data
unique_fields = []

for resource in extracted:
    if resource['resourceType'] not in unique_fields:
        unique_fields.append(resource['resourceType'])
        
uq = sorted(unique_fields)
print(uq)
print(f"\nLength of list: {len(uq)}")