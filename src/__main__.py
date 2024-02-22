import os

from src.pipeline_utils.extract_utils import extract_data
from src.pipeline_utils.transform_utils import transform_data
from src.pipeline_utils.load_utils import load_to_postgres
from src.database.execute_queries import execute_queries
from src.database.create_database import CREATE_DATABASE_QUERY
from src.database.tables_query import CREATE_TABLES_QUERY
from src.config import PATH_TO_DATA
from src.config import PSQL_CREDENTIALS
from src.database.connect import dbconnection

def main():
    """
        Main pipeline function. Executes all steps to extract, transform and load JSON data into a PostgreSQL database.
        All .json files inside 'data' directory will be used.
    """
    # Creates database
    with dbconnection(PSQL_CREDENTIALS, admin_db=True) as conn:
        conn.autocommit = True
        execute_queries(conn, CREATE_DATABASE_QUERY)
    # Creates tables
    with dbconnection(PSQL_CREDENTIALS) as conn:
        execute_queries(conn, CREATE_TABLES_QUERY)
    
    # Data directory
    data_dir = PATH_TO_DATA
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
    