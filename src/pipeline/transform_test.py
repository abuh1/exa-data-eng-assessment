import os
import sys
sys.path.append('Z:\\Documents\\projects\\exa-data-eng-assessment')
from src.pipeline.extract import extract_data
from src.pipeline.transform import transform_data

main_path = os.listdir('data')
json_paths = ['data\\' + p for p in main_path]

extracted = extract_data(json_paths)

resources = transform_data(extracted)
print(resources[0].keys())