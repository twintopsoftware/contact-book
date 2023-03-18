import csv


def menu():
    print("1. Individual Book")
    print("2. Company Book")
    print("3. Exit")


# individual book
def i_book():
    filename = input('Enter the filename of the CSV file to open: ')

    # Read the CSV file into a list of dictionaries
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Function to add a new row to the CSV data
    def create_row():

        id = int(input('Enter a id: '))
        fname = input('Enter an Fname: ')
        lname = input('Enter an Lname: ')
        wp = int(input('Enter a Work Pno: '))
        pp = int(input('Enter a Private Pno: '))
        addr = input('Enter a Address: ')
        new_row = {'id': id, 'FName': fname, 'LName': lname, 'Work Pno': wp, 'Private Pno': pp, 'Address': addr}
        data.append(new_row)

    # Function to read the CSV data
    def read_data():
        for row in data:
            print(row)

    # Function to update a row in the CSV data
    def update_row():
        index = int(input('Enter the index of the row to update: '))
        field = input('Enter the field to update (id, FName,LName,Work Pno,Private Pno,Address): ')
        value = input('Enter the new value: ')
        data[index][field] = value

    # Function to delete a row from the CSV data
    def delete_row():
        index = int(input('Enter the index of the row to delete: '))
        del data[index]

    # Function to save the CSV data to the same file
    def save_data():
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'FName', 'LName', 'Work Pno', 'Private Pno', 'Address']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f'Data saved to {filename}')

    # Main loop to prompt the user for CRUD operations
    while True:
        print('Enter "1" to create a new row')
        print('Enter "2" to read the data')
        print('Enter "3" to update a row')
        print('Enter "4" to delete a row')
        print('Enter "5" to save the data')
        print('Enter "6" to quit')
        choice = input('Enter your choice: ')
        if choice == '1':
            create_row()
        elif choice == '2':
            read_data()
        elif choice == '3':
            update_row()
        elif choice == '4':
            delete_row()
        elif choice == '5':
            save_data()
        elif choice == '6':
            break
        else:
            print('Invalid choice')


# Company book
def c_book():
    filename = input('Enter the filename of the CSV file to open: ')

    # Read the CSV file into a list of dictionaries
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Function to add a new row to the CSV data
    def create_row():

        id = int(input('Enter a id: '))
        cname = input('Enter an Company Name: ')
        addr = input('Enter a Address: ')
        cvrno = int(input('Enter a CVR No: '))
        new_row = {'id': id, 'company name': cname, 'Address': addr, 'CVR no': cvrno}
        data.append(new_row)

    # Function to read the CSV data
    def read_data():
        for row in data:
            print(row)

    # Function to update a row in the CSV data
    def update_row():
        index = int(input('Enter the index of the row to update: '))
        field = input('Enter the field to update (id, company name, CVR no, Address): ')
        value = input('Enter the new value: ')
        data[index][field] = value

    # Function to delete a row from the CSV data
    def delete_row():
        index = int(input('Enter the index of the row to delete: '))
        del data[index]

    # Function to save the CSV data to the same file
    def save_data():
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'Company Name', 'CVR no', 'Address']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f'Data saved to {filename}')

    # def search_data():
    #
    #     search_id = input("Enter the ID to search: ")
    #
    #     # Open the CSV file and search for the ID
    #     with open('c.csv', mode='r') as csv_file:
    #         csv_reader = csv.DictReader(csv_file)
    #         for row in csv_reader:
    #             if row['id'] == search_id:
    #                 print("Record found:")
    #                 print(row)
    #                 break
    #         else:
    #             print("Record not found")

    # Main loop to prompt the user for CRUD operations
    while True:
        print('Enter "1" to create a new row')
        print('Enter "2" to read the data')
        print('Enter "3" to update a row')
        print('Enter "4" to delete a row')
        print('Enter "5" to save the data')
        # print('Enter "6" to search the data')
        print('Enter "6" to quit')
        choice = input('Enter your choice: ')
        if choice == '1':
            create_row()
        elif choice == '2':
            read_data()
        elif choice == '3':
            update_row()
        elif choice == '4':
            delete_row()
        elif choice == '5':
            save_data()
        # elif choice == '6':
        #     search_data()
        elif choice == '7':
            break
        else:
            print('Invalid choice')


while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        i_book()
    elif choice == 2:
        c_book()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")
