import psycopg2

def execute_queries(conn: psycopg2.extensions.connection, queries: list):
    """
        Function that connects to postgresql database using the config.ini file and executes queries passed as a parameter.
        
        Args:
            queries (list): list of SQL queries to execute
    """
    try:
        with conn.cursor() as cursor:
            # Execute each query in the list
            for query in queries:
                cursor.execute(query)
            # Commit the transaction
            conn.commit()
    except (psycopg2.DatabaseError) as error:
        print("Error executing queries:", error)
        
