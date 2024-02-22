from contextlib import contextmanager
import psycopg2

@contextmanager
def dbconnection(credentials: dict, admin_db: bool=False):
    if admin_db:
        connect_db = ''
    else:
        connect_db = credentials['DB_NAME']
    # Database details in config.py
    connection = psycopg2.connect(
                dbname=connect_db,
                user=credentials['DB_USER'],
                password=credentials['DB_PASSWORD'],
                host=credentials['DB_HOST'],
                port=credentials['DB_PORT'])
    try:
        yield connection
    except psycopg2.Error as e:
        print("Failed to connect to the database. Ensure you have adjusted the database details in src/config.py or read instructions on the README if running using Docker.")
    finally:
        connection.close()