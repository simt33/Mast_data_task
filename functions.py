import csv


def read_into_csv(csv_file_name):
    """
    Takes a csv filename as an argument, reads this and returns 2 datasets: headers and rows(data)
    """
    with open(csv_file_name, 'r') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')

        data_raw = []
        for row in readCSV:
            data_raw.append(row)

        headers = data_raw[0]
        data = data_raw[1:]

    return headers, data

