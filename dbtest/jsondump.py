import json
import psycopg2
import sys
sys.path.append('Z:\\Documents\\projects\\exa-data-eng-assessment')
from src.pipeline.extract import extract_data

data = ['data\\Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json']

extracted_data = extract_data(data)
patient_resource = next(extracted_data)

# connect to db
conn = psycopg2.connect(
    dbname='testdb',
    user='postgres',
    password='password',
    host='localhost',
    port='5432',
)

# create a cursor
cur = conn.cursor()

# insert data into the table
sql_insert = """
    INSERT INTO patients (id, resource_type, extension)
    VALUES (%s, %s, %s)
"""

values = (patient_resource['id'], patient_resource['resourceType'], json.dumps(patient_resource['extension']))

# execute sql statement
cur.execute(sql_insert, values)

# commit the transaction
conn.commit()

# close the cursor and connection
cur.close
conn.close