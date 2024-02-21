import psycopg2
from configparser import ConfigParser

# Define a context manager for connecting to the database
class DBConnection:
    def __init__(self):
        self.config_file = 'config.ini'

    def __enter__(self):
        # Read database configuration from config.ini file
        parser = ConfigParser()
        parser.read(self.config_file)
        
        # Read connection parameters
        dbname = parser.get('postgresql', 'dbname')
        user = parser.get('postgresql', 'user')
        password = parser.get('postgresql', 'password')
        host = parser.get('postgresql', 'host')
        port = parser.get('postgresql', 'port')
        
        # Establish a connection to the database
        try:
            self.conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            return self.conn
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")
    
    # Ensures connection closes when done
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()
        # Error handling
        if exc_type:
            print(f"Exception {exc_type} occurred with value: {exc_value}")
        if traceback:
            print(f"Traceback: {traceback}")