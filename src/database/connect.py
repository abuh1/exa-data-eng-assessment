from contextlib import contextmanager
import psycopg2

@contextmanager
def dbconnection(credentials: dict, admin_db: bool=False):
    if admin_db:
        connect_db = ''
    else:
        connect_db = credentials['dbname']
    # Database details in config.py
    connection = psycopg2.connect(
                dbname=connect_db,
                user=credentials['user'],
                password=credentials['password'],
                host=credentials['host'],
                port=credentials['port'])
    try:
        yield connection
    finally:
        connection.close()