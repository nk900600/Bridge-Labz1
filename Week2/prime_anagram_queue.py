"""
 ******************************************************************************
 *  Purpose: to find anagram queue
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week2.prime_number_anagram import PrimeAnagram
from Week2.node_linked_and_sorted import Node, LinkedList
from Week2.util import Queue1


# anagram function
def Anagram_Queue():  # function created

    llist = LinkedList()  # object is created
    q = Queue1()
    anagram = PrimeAnagram()
    try:  # try catch is used to catch error if error
        for data in anagram:
            q.AddRear(llist.Add(data))  # add rear function is used and data is added via linked list
        llist.Print()
        # q.PrintList()       # if we print queue we will data in none as linked list data type is None
    except AttributeError:
        print("check the class file for error")


# main function is created
if __name__ == '__main__':
    Anagram_Queue()
