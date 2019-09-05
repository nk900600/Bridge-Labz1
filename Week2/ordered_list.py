"""
 ******************************************************************************
 *  Purpose: order linked list is printed
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week2.node_linked_and_sorted import LinkedList
from Week1.Utility.utility import ReadFile


# ordered linked list function is created to sort the list
def OrderedList():  # new function for

    items = ReadFile("numbers_1")
    llist1 = LinkedList()
    try:  # try exception is used if any error occurs

        for data in items:  # data is added and printed in linked list format
            llist1.Add(data)
        llist1.sortlist()

    except AttributeError:
        print("check the class attribute ")


# main function is created
if __name__ == '__main__':
    OrderedList()
