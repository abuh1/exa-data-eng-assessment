import os
import time
import argparse

from src.pipeline_utils.extract_utils import extract_data
from src.pipeline_utils.transform_utils import transform_data
from src.pipeline_utils.load_utils import load_to_postgres
from src.database.execute_queries import execute_queries
from src.database.connect import dbconnection
from src.database.create_database import create_database_query
from src.database.tables_query import create_tables_query
from src.config import PATH_TO_DATA
from src.config import psql_credentials


def main():
    """
        Main pipeline function. Executes all steps to extract, transform and load JSON data into a PostgreSQL database.
        All .json files inside 'data' directory will be used.
    """
    start_time = time.time()
    
    # Change data path if using docker
    if os.environ.get('DOCKER_CONTAINER'):
        data_dir = 'data/'
    else:
        data_dir = PATH_TO_DATA
    
    # Creates database
    with dbconnection(psql_credentials, admin_db=True) as conn:
        print("Connected to server...")
        conn.autocommit = True
        execute_queries(conn, create_database_query)
        print("Created database...")
    # Creates tables
    with dbconnection(psql_credentials) as conn:
        execute_queries(conn, create_tables_query)
        print("Created relations...")
        print("Connection closed.")
    
    # List of only JSON files in the directory
    json_files = [file for file in os.listdir(data_dir) if file.endswith('.json')]
    # Create a list of absolute file paths
    json_file_paths = [os.path.join(data_dir, file) for file in json_files]
    
    # Extract all JSON files' data
    print("Extracting data...")
    ex = extract_data(json_file_paths)
    # Transform all extracted data
    print("Transforming data...")
    transformed_data = transform_data(ex)
    # Load the transformed_data into the PostgreSQL database.
    print("Loading data to database...")
    load_to_postgres(transformed_data)
    
    end_time = time.time()
    print(f"All data successfully extracted, transformed and loaded in {end_time-start_time} seconds")
    
if __name__ == '__main__':
    main()
    