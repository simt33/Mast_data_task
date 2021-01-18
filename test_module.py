import unittest
from functions import *


class TestCSVImport(unittest.TestCase):

    def setUp(self):
        self.csv_file = "mock_data.csv"

    def test_read_into_csv_valid_import(self):
        headers, data = read_into_csv(self.csv_file)
        self.assertEqual(headers, ['Header 1', 'Header 2'])
        self.assertEqual(data, [['a', 'b'], ['foo', 'bar']])


if __name__ == '__main__':
    unittest.main()