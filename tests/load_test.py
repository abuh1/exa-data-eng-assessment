import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from src.pipeline_utils.load_utils import load_to_postgres

class TestLoadToPostgres(unittest.TestCase):

    @patch('src.pipeline_utils.load_utils.dbconnection')
    def test_load_to_postgres(self, mock_dbconnection):
        # Mock data
        data = [
            {'resource_type': 'table1', 'col1': 'value1', 'col2': 'value2'},
            {'resource_type': 'table2', 'col3': 'value3', 'col4': 'value4'}
        ]

        # Mock cursor and connection objects
        mock_cursor = MagicMock()
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_dbconnection.return_value.__enter__.return_value = mock_conn

        # Call the function
        load_to_postgres(data)

        # Assert that the expected queries are executed
        expected_queries = [
            "COPY table1 (col1,col2) FROM STDIN WITH CSV",
            "COPY table2 (col3,col4) FROM STDIN WITH CSV"
        ]
        for call_args, expected_query in zip(mock_cursor.copy_expert.call_args_list, expected_queries):
            self.assertEqual(call_args[0][0], expected_query)

if __name__ == '__main__':
    unittest.main()