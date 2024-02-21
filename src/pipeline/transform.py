import itertools
import inflection
from io import StringIO
from collections import defaultdict

from database.connect import DBConnection

# This function connects to a database with credentials inside 'config.ini'
def transform_data(extracted_data):
    """
        Main transform function. Takes data outputted by 'extract' (generator object containing all patients' data)
        and flattens the data. Connects to database using config.ini and retrieves column names which then matches
        the data to the column names and retrieves the data needed.
        
        Args:
            extracted_data (generator object): Data extracted from json files using 'extract' module.
        
    """
    # Grab all resources from extracted json files.
    resources_gen = grab_all_resources(extracted_data)
    
    # Flatten all resources 
    resources_list = list(resources_gen)
    for i, d in enumerate(resources_list):
        flat = flatten_dict(d)
        resources_list[i] = flat
    
    # Convert all dictionary keys to snake case (to match postgresql column names)
    for d in resources_list:
        snake_case_dict = {inflection.underscore(key): value for key, value in d.items()}
        # Snake case the value of 'resource_type' as well, as these will match with the database tables
        snake_case_resource_type = inflection.underscore(snake_case_dict['resource_type'])
        snake_case_dict['resource_type'] = snake_case_resource_type
        d.clear()
        d.update(snake_case_dict)
    
    # List of final resources that will be appended to
    filtered_resources = []
    # Grabs each dictionary's corresponding table column names from the database, and discards the items that aren't needed in the table.
    with DBConnection() as conn:
        for resource in resources_list:
            # Get the name of the table that the current resource will fill
            table_name = resource['resource_type']
            column_names = get_column_names(conn, table_name)
            final_dict = filter_dict_entry(resource, column_names)
            filtered_resources.append(final_dict)
    
    return filtered_resources

# Filters a dictionary to retrieve items matching database table columns
def filter_dict_entry(data: dict, column_names):
    filtered_dict = {key: value for key, value in data.items() if key in column_names}
    return filtered_dict

# Recursive function to flatten nested dictionaries within a single json dictionary
def flatten_dict(data_dict: dict, parent_key='', seperator='_'):
    """
        Flatten a dictionary with nested values.
    
        Args:
            data_dict (dict): Nested dictionary to flatten.
            parent_key: current parent key for the nested dictionary value.
            seperator: seperating string for new flattened key.
            
        Returns:
            Flattened version of the input dictionary. 
    """
    items = []
    for k, v in data_dict.items():
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
    
# Utilises grab_resources on all json files, yielding a bigger generator with all resources from all patients.
def grab_all_resources(extracted_data):
    # Chaining generator function to extend it
    combined_gen = (generate_resources(d) for d in extracted_data)
    combined_resources = itertools.chain(*combined_gen)
    return combined_resources

# This function is just for grabbing all resources from only one json file.
def generate_resources(data):
    """
        Grabs every 'resource' from one patient file.
        
        Args:
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

# Function to retrieve column names from database tables - used in main transform_data method.
def get_column_names(conn, table_name):
    with conn.cursor() as cursor:
        cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = %s", (table_name,))
        columns = [row[0] for row in cursor.fetchall()]
        return columns
    