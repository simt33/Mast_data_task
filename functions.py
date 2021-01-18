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


def user_input():
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

    if user_input_text == "1":
        pass
    elif user_input_text == "2":
        pass
    elif user_input_text == "3":
        pass
    elif user_input_text == "4":
        pass
    else:
        user_input()
