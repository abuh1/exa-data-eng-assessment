import json
import csv
from io import StringIO

from src.database.connect import dbconnection
from src.config import psql_credentials

# Changed data to format suitable for loading, then loads using COPY method from postgres
def load_to_postgres(data: list):
    # Connect to database
    with dbconnection(psql_credentials) as conn:
        print("Connected to server...")
        cursor = conn.cursor()
        try:
            # Group data by table name
            table_rows = group_table_data(data)

            # Insert data into tables using COPY query
            for table_name, rows in table_rows.items():
                # Get column names for the table (top-level keys)
                cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = N'{table_name}' ORDER BY ordinal_position")
                db_columns = [row[0] for row in cursor.fetchall()]

                # Create a file-like object in memory
                data_file = StringIO()
                
                # Create a CSV writer
                csv_writer = csv.writer(data_file, quoting=csv.QUOTE_MINIMAL)

                # Construct CSV-style data for each row
                for row in rows:
                    row_data = []
                    for col in db_columns:
                        if col in row:
                            value = row[col]
                            # Serialize value if it's a dictionary or list
                            if isinstance(value, (dict, list)):
                                value = json.dumps(value)
                            row_data.append(value)
                        else:
                            row_data.append('')
                    # Write the row to the CSV file
                    csv_writer.writerow(row_data)
                
                # Move file pointer to the beginning
                data_file.seek(0)
                
                # Execute the COPY command
                copy_statement = f"COPY {table_name} ({','.join(db_columns)}) FROM STDIN WITH CSV"
                cursor.copy_expert(copy_statement, data_file)
                conn.commit()
                
        except Exception as e:
            conn.rollback()
            print(f"Error loading data into table {table_name}: {e}")
            
        print("Connection closed.")
    

# Function to group table data; returns dictionary
def group_table_data(data):
    # Group data by table name
    table_rows = {}
    for row in data:
        if row.get('resource_type'):
            table_name = row['resource_type']
        else:
            # Skip processing for rows where 'resource_type' is not present or empty
            continue
        if table_name:
            if table_name not in table_rows:
                table_rows[table_name] = []
            table_rows[table_name].append(row)
    
    return table_rows