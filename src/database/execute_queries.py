import psycopg2

from connect import DBConnection

def execute_queries(queries: list, config_file_path):
    """
        Function that connects to postgresql database using the config.ini file and executes queries passed as a parameter.
        
        Args:
            queries (list): list of SQL queries to execute
    """
    try:
        with DBConnection(config_file=config_file_path) as conn:
            cursor = conn.cursor()
            # Execute each query in the list
            for query in queries:
                cursor.execute(query)
            # Commit the transaction
            conn.commit()
        print("Queries executed successfully!")    
    except (psycopg2.DatabaseError) as error:
        print("Error executing queries:", error)
        
