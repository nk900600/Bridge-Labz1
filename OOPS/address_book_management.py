"""
 ******************************************************************************
 *  Purpose:  Address book management will take user input and will add or remove
 *            data as per user intentions
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from OOPS.oops_util import AddressBook


# Address book is created to store the user info
def Addressbook_Management():

    while True:
        address = AddressBook("address_book_json")
        try:  # try function is used for catching error if any
            # user input is taken
            userdata = int(input("\nNumber of data you wish to add or delete\nUser Input: "))
            if userdata >= 10:
                print("enter the number below 4")
                continue

            for i in range(userdata):
                user = int(input("""\n1  Add\n2  Delete\
    \n3  Exit \n4  Print in Mailing Format\nUser Input :"""))
                if user >= 5:
                    print("enter below 5")
                    continue

                # if user input is 1 then a new data will be ad`ded to the address book
                if user == 1:
                    address.Add()  # here new data is added and printed out

                # if user input is 2 then one of the data will be deleted
                if user == 2:
                    print(address.Only_Names())  # name on the address book will be listed out
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
        except (ValueError,UnboundLocalError):  # if any value error is occurred while entering the data then below
            # statement will print
            print("check the input")


# main function is called
if __name__ == '__main__':
    Addressbook_Management()
