import unittest
from unittest.mock import patch, MagicMock
from src.database.connect import dbconnection

class TestDBConnection(unittest.TestCase):

    @patch('src.database.connect.psycopg2.connect')
    def test_dbconnection(self, mock_connect):
        # Mock credentials
        credentials = {
            'dbname': 'test_db',
            'user': 'test_user',
            'password': 'test_password',
            'host': 'test_host',
            'port': 'test_port'
        }

        # Call the function
        with dbconnection(credentials) as conn:
            pass

        # Assert that psycopg2.connect was called with the correct arguments
        mock_connect.assert_called_once_with(
            dbname='test_db',
            user='test_user',
            password='test_password',
            host='test_host',
            port='test_port'
        )

if __name__ == '__main__':
    unittest.main()