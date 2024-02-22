import unittest
from unittest.mock import mock_open, patch
from src.pipeline_utils.extract_utils import extract_data

class TestExtract(unittest.TestCase):
    # Define a test case for the extract_data function
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_extract_data(self, mock_open):
        # Define the list of json files to be processed
        json_files = ['file1.json', 'file2.json']

        # Call the extract_data function with the list of json files
        generator = extract_data(json_files)

        # Iterate through the generator and check if data is extracted correctly
        for data in generator:
            self.assertIsInstance(data, dict)  # Ensure extracted data is a dictionary

        # Assert that the open function was called with the correct arguments
        mock_open.assert_any_call('file1.json', 'r', encoding='utf-8')
        mock_open.assert_any_call('file2.json', 'r', encoding='utf-8')

if __name__ == '__main__':
    unittest.main()