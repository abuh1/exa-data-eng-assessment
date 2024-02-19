import psycopg2
from configparser import ConfigParser

# Define a context manager for connecting to the database
class DBConnection:
    def __init__(self, config_file):
        self.config_file = config_file

    def __enter__(self):
        # Read database configuration from config.ini file
        parser = ConfigParser
        parser.read(self.config_file)
        
        # Read connection parameters
        dbname = parser.get('postgresql', 'dbname')
        user = parser.get('postgresql', 'user')
        password = parser.get('postgresql', 'password')
        host = parser.get('postgresql', 'host')
        port = parser.get('postgresql', 'port')
        
        # Establish a connection to the database
        self.conn = psycopg2.connnect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return self.conn
    
    # Ensures connection closes when done
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()
        # Error handling
        if exc_type is not None:
            print(f"Exception occurred: {exc_type}, {exc_value}")