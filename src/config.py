import os
# PostgreSQL credentials
psql_credentials = {
    'DB_USER': 'postgres',          # Username for the database
    'DB_PASSWORD': 'password',      # Password for the database
    'DB_NAME': 'health_resources',  # Name of the database you wish to connect to
    'DB_HOST': '127.0.0.1',         # Host server
    'DB_PORT': '5432'}              # Port for the database

# Change PSQL credentials if environment variables are passed.
for key in psql_credentials:
    env_var_value = os.getenv(key)
    if env_var_value:
        psql_credentials[key] = env_var_value

# Data path
PATH_TO_DATA = 'Z:\\Documents\\projects\\exa-data-eng-assessment\\test_data'