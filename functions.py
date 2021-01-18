import csv


def read_into_csv(csv_file_name):
    """
    Takes a csv filename as an argument, reads this and returns 2 datasets: headers and rows(data).
    """
    with open(csv_file_name, 'r') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')

        data_raw = []
        for row in readCSV:
            data_raw.append(row)

        headers = data_raw[0]
        data = data_raw[1:]

    return headers, data


def user_input(data, headers):
    """
    Requests user input and calls appropriate function.
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
    print ("\n")

    if user_input_text == "1":
        print (headers)
        [print (row) for row in bottom5_rent(data)]
        user_input(data, headers)

    elif user_input_text == "2":
        data_25yr_lease = get_25yr_lease(data)
        total_current_rent = sum([float(row[10]) for row in data_25yr_lease])
        print (headers)
        [print (row) for row in data_25yr_lease]
        print ("\nTotal Current Rent: " + str(total_current_rent))

    elif user_input_text == "3":
        pass
    elif user_input_text == "4":
        pass
    else:
        user_input(data, headers)


def bottom5_rent(data):
    """
    Returns the bottom 5 records by Current Rent.
    """

    sorted_data = sorted(data, key=lambda x: float(x[10]))

    return sorted_data[:5]


def get_25yr_lease(data):
    """
    Returns all record where Lease is equal to 25 years.
    """

    data_lease = []
    for row in data:
        if int(row[9]) == 25:
            data_lease.append(row)

    return data_lease
