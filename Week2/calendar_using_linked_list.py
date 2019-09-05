"""
 ******************************************************************************
 *  Purpose: Calender_Using_Linked_List
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week2.node_linked_and_sorted import LinkedList
from Week2.calender import calender
from Week2.util import Queue1


# Calender_Using_Linked_List function is created
def Calender_Using_Linked_List():  # function is created
    while True:
        try:
            llist = LinkedList()  # object is created for imported classes
            q = Queue1()
            month = int(input("which month's calender u wish to see in MM format :"))
            if month <= 0 or month >= 13:
                print("enter between 0 and 13")
                continue

            year = int(input("for which year YYYY format"))
            if year <= 1000 or year >= 3000:
                print("enter between 1000 and 3000")
                continue

            array = calender(month, year)
            # try is used for locating the error
            for items in array:  # for loop is used using adding data in linked list
                for data in items:
                    q.AddRear(llist.Add(data))  # data is added in the linked list via queue class

            llist.PrintCalendar()  # now calendar is printed in linked list
            break

        except ValueError:  # exception will find the error
            print("please check the input ")


# main function is called
if __name__ == '__main__':
    Calender_Using_Linked_List()  # now function is called
