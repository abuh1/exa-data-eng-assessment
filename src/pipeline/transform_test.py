import os
import sys
import time
sys.path.append('Z:\\Documents\\projects\\exa-data-eng-assessment')
from src.pipeline.extract import extract_data
from src.pipeline.transform import transform_data
from src.pipeline.load import load_to_postgres

start_time = time.time()

main_path = os.listdir('data')
json_paths = ['data\\' + p for p in main_path]

extracted = extract_data(json_paths)

resources = transform_data(extracted)

load_to_postgres(resources)