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


class TestDataFunctions(unittest.TestCase):

    def setUp(self):
        self.data = [
            ['Rue Gilmotte', 'Paris', 'France','' ,'' , 'Unit1', 'Company1', '05 Jan 1993', '15 Jan 2008', '18', '12532.80'],
            ['Rue Lafayette', 'Grenoble', 'France', 'Europe', '', 'Unit2', 'Company2', '25 Apr 1998', '15 Jan 2015', '69', '11331.20'],
            ['Rue Perle', 'Lyon', 'France', 'Europe', '', 'Unit3', 'Company2', '01 Apr 1999', '30 Sep 2020',
             '45', '12903.00'],
            ['Calle de la Mancha', 'Spain', 'Madrid', 'Europe', '', 'Unit4', 'Company4', '25 Apr 1998', '15 Jan 2015',
             '55', '14214.00'],
            ['Calle de la Bruja', 'Spain', 'Valencia', '', '', 'Unit5', 'Company2', '10 Apr 2018', '18 Jul 2019',
             '25', '11452.23'],
            ['Calle del sol', 'Spain', 'Salamanca', '', '', 'Unit6', 'Company1', '14 May 2000', '12 Jan 2017',
             '14', '14342.00'],
            ['Calle del fuego', 'Spain', 'Barcelona', 'Europa', '', 'Unit7', 'Company6', '12 May 1998', '12 Jan 2016',
             '25', '13314.00'],
        ]

    def test_bottom5_rent(self):
        data_bottom5_rent = bottom5_rent(self.data)
        self.assertEqual(data_bottom5_rent.len(), 5)
        self.assertEqual(data_bottom5_rent[0][0], 'Rue Lafayette')
        self.assertEqual(data_bottom5_rent[1][10], '11452.23')


if __name__ == '__main__':
    unittest.main()
