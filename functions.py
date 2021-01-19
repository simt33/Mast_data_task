import csv
from datetime import datetime


def read_into_csv(csv_file_name):
    """
    Takes a csv filename as an argument, reads this and returns 2 datasets: headers and rows(data).
    """
    with open(csv_file_name, 'r') as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')

        data_raw = []
        for row in read_csv:
            data_raw.append(row)

        headers = data_raw[0]
        data = data_raw[1:]

    return headers, data


def user_input(data, headers):
    """
    Requests user input and prints relevant information. Always recalls another user_input (apart from quit).
    Takes arguments data (list) and headers (list).
    """

    user_input_text = """
    
Please enter a number to continue
1. View bottom 5 records by current rent
2. View mast data where Lease = 25 years (including Total Current Rent)
3. View # of masts per tenant
4. View data for rentals where Lease Start date is between 1st June 1999 and 31st August 2007
5. Quit program

>> """
    user_input_text = input(user_input_text)
    print("\n")

    if user_input_text == "1":
        # prints bottom 5 records by rent. Recalls user input.

        print(headers)
        [print(row) for row in bottom5_rent(data)]

        user_input(data, headers)

    elif user_input_text == "2":
        # prints all records where lease = 25, as well as Total Current Rent. Recalls user input.

        data_25yr_lease = get_25yr_lease(data)
        total_current_rent = sum([float(row[10]) for row in data_25yr_lease])

        print(headers)
        [print(row) for row in data_25yr_lease]
        print("\nTotal Current Rent: " + str(total_current_rent))

        user_input(data, headers)

    elif user_input_text == "3":
        # prints tenants and mast counts, in alphabetical order. Recalls user input

        mast_dict = count_of_masts(data)

        print("Number of masts per tenant: \n")
        [print(str(value) + " : " + key) for key, value in sorted(mast_dict.items(), key=lambda item: item[0])]

        user_input(data, headers)

    elif user_input_text == "4":
        # prints records where dates are between 01/06/1999 and 31/08/2007

        print(headers)
        [print(row) for row in compare_dates(data)]

        user_input(data, headers)

    elif user_input_text == "5":
        quit()

    else:
        print("\nInvalid input")
        user_input(data, headers)


def bottom5_rent(data):
    """
    Returns the bottom 5 records by Current Rent as a list.
    Takes in data as a list.
    """

    sorted_data = sorted(data, key=lambda x: float(x[10]))

    return sorted_data[:5]


def get_25yr_lease(data):
    """
    Returns all record where Lease is equal to 25 years as a list.
    Takes in data as a list.
    """

    data_lease = []
    for row in data:
        if int(row[9]) == 25:
            data_lease.append(row)

    return data_lease


def count_of_masts(data):
    """
    Returns a dictionary of tenant names against count of masts as a dictionary.
    Takes data as a list.
    """

    masts_dict = {}
    for row in data:
        if row[6] in masts_dict.keys():
            masts_dict[row[6]] += 1
        else:
            masts_dict[row[6]] = 1

    return masts_dict


def compare_dates(data):
    """
    Returns a list of records where Lease Start Date is between 1st June 1999 and 31st August 2007. Converts all dates
    to dd/mm/YYYY format.
    Takes data as a list.
    """

    min_date = datetime.strptime("01/06/1999", "%d/%m/%Y")
    max_date = datetime.strptime("31/08/2007", "%d/%m/%Y")

    data_by_date = []

    for row in data:
        date_start_lease = datetime.strptime(row[7], "%d %b %Y")
        if min_date <= date_start_lease <= max_date:
            date_end_lease = datetime.strptime(row[8], "%d %b %Y")
            row[7] = datetime.strftime(date_start_lease, "%d/%m/%Y")
            row[8] = datetime.strftime(date_end_lease, "%d/%m/%Y")
            data_by_date.append(row)

    return data_by_date
