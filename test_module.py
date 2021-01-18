import unittest
from functions import *


class TestCSVImport(unittest.TestCase):

    def setUp(self):
        self.csv_file = "mock_data_IMPORT.csv"

    def test_read_into_csv_valid_import(self):
        headers, data = read_into_csv(self.csv_file)
        self.assertEqual(headers, ['Header 1', 'Header 2'])
        self.assertEqual(data, [['a', 'b'], ['foo', 'bar']])


class TestUserInput(unittest.TestCase):
    # My understanding is that unittest.mock can be used to mimic user input, but I'm not sure how this would
    # be implemented, so I have left this section blank.
    pass


if __name__ == '__main__':
    unittest.main()