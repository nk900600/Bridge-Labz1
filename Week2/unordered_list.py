"""
 ******************************************************************************
 *  Purpose: to print Prime Anagram
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week2.node_linked_and_sorted import LinkedList
from Week1.Utility.utility import ReadFile


# main function is created
def UnorderedlList():  # new function for linked list

    items = ReadFile("numbers")
    llist = LinkedList()
    try:       # try exception is used for the finding the error
        for data in items:  # data is added and printed in linked list format
            llist.Add(data)
    except AttributeError:   # error is catched if any
        print("please check the error ")
    llist.Print()


# main function is created
if __name__ == '__main__':
    UnorderedlList()
