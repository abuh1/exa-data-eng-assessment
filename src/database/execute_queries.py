import psycopg2
from .connect import DBConnection
from .tables_query import CREATE_TABLES_QUERY

# Connects to a database and creates the tables from the query file
def execute_queries(query):
    # Connect to the database (edit your database connection details in the config.ini file in the root directory)
    config_file = 'config.ini'
    with DBConnection(config_file) as conn:
        cursor = conn.cursor()
        # Check isinstance for query
        