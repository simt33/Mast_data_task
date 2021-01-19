from functions import *


csv_file = "data/Python Developer Test Dataset.csv"

headers, data = read_csv_into_lists(csv_file)
reformat_dates(data)

user_input(data, headers)
