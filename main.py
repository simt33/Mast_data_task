from functions import *


csv_file = "Python Developer Test Dataset.csv"

headers, data = read_into_csv(csv_file)

user_input(data, headers)
