
"""
 ******************************************************************************
 *  Purpose: Calender printing
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import ReadFile
from Week2.util import Hashing
from Week2.node_linked_and_sorted import LinkedList


# Hashing file function is created and
def HashingFile():  # hashing function is used for hashing the file

    hash = Hashing()     # object is created for the class
    llist = LinkedList()
    it = ReadFile("key")   # data is read from the file
    data = []      # file data is iterated below and appended in the data array
    for i in it:
        data.append(int(i))
    # print(data)
    try:  # try function is used for catching the exceptions to handle exceptions
        for i in data:  # we have added data in hash table by calling insert function
            hash.Insert(i)
        for i in hash.Print():    # now hash file is add to the liked list
            llist.Add(i)
        # print(hash.print())  # hash table will print
        llist.Print()  # now linked list from hash table will be printed

    except AttributeError:     # if any error it will below statement
        print("please check the class file ")


"""
main is function is created
"""


if __name__ == '__main__':
    HashingFile()
