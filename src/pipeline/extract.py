import json

# Generator function yielding all data for each json file in the directory
def extract_data(json_files: list):
    """ Extracts all data from the JSON files in the directory.
    
        Parameters:
            json_files (list): List of paths of json files. 
        
        Yields:
            extracted_data (generator object): Generator object containing data from all json files in the directory.
    """
    # Yields all 'resource' from each entry for each patient
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for entry in data['entry']:
                    resource = entry['resource']
                    yield resource
        except FileNotFoundError:
            print(f"Error: File {json_file} not found")
        except json.JSONDecodeError:
            print(f"Error: Unable to decode JSON in file {json_file}")
            
