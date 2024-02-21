import os

from src.pipeline_utils.extract_utils import extract_data
from src.pipeline_utils.transform_utils import transform_data
from src.pipeline_utils.load_utils import load_to_postgres

def main():
    """
        Main pipeline function. Executes all steps to extract, transform and load JSON data into a PostgreSQL database.
        All .json files inside 'data' directory will be used.
    """
    # Data directory
    data_dir = 'data'
    # List of only JSON files in the directory
    json_files = [file for file in os.listdir(data_dir) if file.endswith('.json')]
    # Create a list of absolute file paths
    json_file_paths = [os.path.join(data_dir, file) for file in json_files]
    
    # Extract all JSON files' data
    ex = extract_data(json_file_paths)
    # Transform all extracted data
    transformed_data = transform_data(ex)
    # Load the transformed_data into the PostgreSQL database.
    load_to_postgres(transformed_data)
    
if __name__ == '__main__':
    main()
    