import psycopg2

# Connect to PostgreSQL (adjust credentials as needed)
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='password',
    host='localhost',
    port='5432'
)

# Create a cursor
cur = conn.cursor()

# Switch to the new database
conn.close()
conn = psycopg2.connect(
    dbname='testdb',
    user='postgres',
    password='password',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

# Define SQL table schema and create tables
create_table_query = """
CREATE TABLE patients (
  id VARCHAR(45) PRIMARY KEY,
  resource_type VARCHAR(50),
  resource_id VARCHAR(36),
  extension JSONB,
  identifier JSONB,
  name JSONB,
  telecom JSONB,
  gender VARCHAR(10),
  birth_date VARCHAR(10),
  address JSONB,
  marital_status_text VARCHAR(20),
  multiple_birth_boolean VARCHAR(5),
  communication JSONB
);
"""

# Execute the SQL query to create the tables
cur.execute(create_table_query)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()