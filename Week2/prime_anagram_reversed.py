
"""
 ******************************************************************************
 *  Purpose: to find Anagram_Reversed
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week2.prime_number_anagram import PrimeAnagram
from Week2.node_linked_and_sorted import Node,LinkedList
from Week2.util import Stack


# anagram reversed function is created
def Anagram_Reversed():   # function created

    llist = LinkedList()  # object is created
    stack = Stack()
    anagrams = PrimeAnagram()

    try:       # try exception is used for the finding the error
        for data in anagrams[::-1]:
            stack.Push(llist.Add(data))   # push function is used and data is pushed via linked list
        llist.Print()
        # print(stack.size())  # if we print stack we will data in none as linked list data type is None

    except AttributeError:     # if error found exception is print the below statement
        print("please check class file  ")


# main function is created
if __name__ == '__main__':
    Anagram_Reversed()





