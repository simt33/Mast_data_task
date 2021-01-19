import unittest
from functions import *


# test_data is defined once and then pulled in by each data function to make dataset easy to modify if necessary
test_data_reformatted = [
            ['Rue Gilmotte', 'Paris', 'France', '', '', 'Unit1', 'Company1', '05/01/1993', '15/01/2008',
             '18', '12532.80'],
            ['Rue Lafayette', 'Grenoble', 'France', 'Europe', '', 'Unit2', 'Company2', '25/04/1998', '15/01/2015',
             '69', '11331.20'],
            ['Rue Perle', 'Lyon', 'France', 'Europe', '', 'Unit3', 'Company2', '01/08/1999', '30/09/2020',
             '45', '12903.00'],
            ['Calle de la Mancha', 'Spain', 'Madrid', 'Europe', '', 'Unit4', 'Company4', '25/04/1998', '15/01/2015',
             '55', '14214.00'],
            ['Calle de la Bruja', 'Spain', 'Valencia', '', '', 'Unit5', 'Company2', '10/04/2018', '18/07/2019',
             '25', '11452.23'],
            ['Calle del Sol', 'Spain', 'Salamanca', '', '', 'Unit6', 'Company1', '14/05/2000', '12/01/2017',
             '14', '14342.00'],
            ['Calle del Fuego', 'Spain', 'Barcelona', 'Europa', '', 'Unit7', 'Company6', '12/05/1998', '12/01/2016',
             '25', '13314.00'],
            ]


class TestCSVImport(unittest.TestCase):

    def setUp(self):
        self.csv_file = "data/mock_data_IMPORT.csv"

    def test_read_csv_into_lists_valid_headers(self):
        headers, data = read_csv_into_lists(self.csv_file)
        self.assertEqual(headers, ['Header 1', 'Header 2'])

    def test_read_csv_into_lists_valid_data(self):
        headers, data = read_csv_into_lists(self.csv_file)
        self.assertEqual(data, [['a', 'b'], ['foo', 'bar']])


class TestReformatDates(unittest.TestCase):

    def setUp(self):
        self.data = test_data = [
            ['Rue Gilmotte', 'Paris', 'France', '', '', 'Unit1', 'Company1', '05 Jan 1993', '15 Jan 2008',
             '18', '12532.80'],
            ['Rue Lafayette', 'Grenoble', 'France', 'Europe', '', 'Unit2', 'Company2', '25 Apr 1998', '15 Jan 2015',
             '69', '11331.20'],
            ['Rue Perle', 'Lyon', 'France', 'Europe', '', 'Unit3', 'Company2', '01 Aug 1999', '30 Sep 2020',
             '45', '12903.00'],
            ['Calle de la Mancha', 'Spain', 'Madrid', 'Europe', '', 'Unit4', 'Company4', '25 Apr 1998', '15 Jan 2015',
             '55', '14214.00'],
            ['Calle de la Bruja', 'Spain', 'Valencia', '', '', 'Unit5', 'Company2', '10 Apr 2018', '18 Jul 2019',
             '25', '11452.23'],
            ['Calle del Sol', 'Spain', 'Salamanca', '', '', 'Unit6', 'Company1', '14 May 2000', '12 Jan 2017',
             '14', '14342.00'],
            ['Calle del Fuego', 'Spain', 'Barcelona', 'Europa', '', 'Unit7', 'Company6', '12 May 1998', '12 Jan 2016',
             '25', '13314.00'],
            ]

    def test_reformat_date_lease_start(self):
        reformat_dates(self.data)
        self.assertEqual(self.data[0][7], '05/01/1993')

    def test_reformat_date_lease_end(self):
        reformat_dates(self.data)
        self.assertEqual(self.data[2][8], '30/09/2020')


class TestUserInput(unittest.TestCase):
    # My understanding is that unittest.mock can be used to mimic user input, but I'm not sure how this would
    # be correctly implemented, so I have left this section blank for now.
    pass


class TestBottom5(unittest.TestCase):

    def setUp(self):
        self.data = test_data_reformatted

    def test_bottom5_rent_check_length(self):
        data_bottom5_rent = bottom5_rent(self.data)
        self.assertEqual(len(data_bottom5_rent), 5)

    def test_bottom5_rent_check_value_1(self):
        data_bottom5_rent = bottom5_rent(self.data)
        self.assertEqual(data_bottom5_rent[0][0], 'Rue Lafayette')

    def test_bottom5_rent_check_value_2(self):
        data_bottom5_rent = bottom5_rent(self.data)
        self.assertEqual(data_bottom5_rent[1][10], '11452.23')


class Test25yrLease(unittest.TestCase):

    def setUp(self):
        self.data = test_data_reformatted

    def test_25yr_lease_check_length(self):
        data_25yr_lease = get_25yr_lease(self.data)
        self.assertEqual(len(data_25yr_lease), 2)

    def test_25yr_lease_check_value_1(self):
        data_25yr_lease = get_25yr_lease(self.data)
        self.assertEqual(data_25yr_lease[0][0], 'Calle de la Bruja')

    def test_25yr_lease_check_value_2(self):
        data_25yr_lease = get_25yr_lease(self.data)
        self.assertEqual(data_25yr_lease[1][9], '25')


class TestCountOfMasts(unittest.TestCase):

    def setUp(self):
        self.data = test_data_reformatted

    def test_count_of_masts_check_is_dict(self):
        data_count_of_masts = count_of_masts(self.data)
        self.assertIsInstance(data_count_of_masts, dict)

    def test_count_of_masts_check_value_1(self):
        data_count_of_masts = count_of_masts(self.data)
        self.assertEqual(data_count_of_masts['Company2'], 3)

    def test_count_of_masts_check_length(self):
        data_count_of_masts = count_of_masts(self.data)
        self.assertEqual(len(data_count_of_masts.items()), 4)

    def tearDown(self):
        self.data = []


class TestCompareDates(unittest.TestCase):

    def setUp(self):
        self.data = test_data_reformatted

    def test_compare_dates_check_length(self):
        data_compare_dates = compare_dates(self.data)
        self.assertEqual(len(data_compare_dates), 2)

    def test_compare_dates_check_value_1(self):
        data_compare_dates = compare_dates(self.data)
        self.assertEqual(data_compare_dates[0][0], 'Rue Perle')

    def test_compare_dates_check_lengths(self):
        data_compare_dates = compare_dates(self.data)
        self.assertEqual(len(data_compare_dates), 2)


if __name__ == '__main__':
    unittest.main()
