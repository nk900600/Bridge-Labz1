from OOPS.oops_util import AddressBook

"""
address book function is created for adding, deleting, sorting and printing data
"""


def addressbook_management():
    while True:
        address = AddressBook("address_book_json")

        try:  # try function is used for catching error if any
            # user input is taken
            userdata = int(input("number of data you want to delete or add :"))
            if userdata >= 10:
                print("enter the number below 10")
                continue
            for i in range(userdata):

                user = int(input("""\npress 1 to add\npress 2 to delete\
    \npress 3 to  exit \npress 4 to print in mailing format
                                   \nuser input :"""))
                if user >= 5:
                    print("enter below 5")
                    continue

                # if user input is 1 then a new data will be ad`ded to the address book
                if user == 1:
                    print(address.Add()[1])  # here new data is added and printed out

                # if user input is 2 then one of the data will be deleted
                if user == 2:
                    address.Only_Names()  # name on the address book will be listed out
                    address.Delete()  # here name will be deleted

                # if user input is 3  then address book will be sorted and dump back to the json file
                if user == 3:

                    print("program ended")
                    return

                # if user inputs 4 then data is printed in mailing format
                elif user == 4:

                    address.Print()  # here data is printed

                # else below statement will be printed

                address.Sort()  # here sorting function is used
                print("\ndata is sorted which can be seen in json file ")
                address.Dump("address_book_json")
                break

        except ValueError:  # if any value error is occurred while entering the data then below statement will print
            print("check the input")


"""
main function is created to call address book function
"""

if __name__ == '__main__':
    addressbook_management()