"""
 ******************************************************************************
 *  Purpose: util for queue,hashing and stack classes
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week2.node_linked_and_sorted import LinkedList
from Week1.Utility.utility import PrimeNumber


# queue class is created
class Queue:
    """
    queue class is created with different attribution
    """

    # queue class made with all attribution
    def __init__(self):
        self.ul = LinkedList()
        self.items = []

    def IsEmpty(self):  # is empty function is used to check size of the list
        return self.items == []

    def Enqueue(self, data):  # enqueue is used for the inserting data in array
        self.items.insert(0, data)

    def Size(self):  # size function is used for checking the size of the array
        return len(self.items)

    def Dequeue(self):  # de-queue is used remove data from queue
        self.items.pop()


# queue class is again created
class Queue1:
    """
    queue called is created with different attribution
    """

    def __init__(self):  # queue is used for linked list as linked list is called in queue
        self.ul = LinkedList()
        self.items = []

    def Dequeue(self):  # de-queue is used for popping data from queue
        self.items.pop()

    def AddRear(self, data):  # add gear is used for adding data at the end for the array
        self.items.insert(0, data)
        return self.ul.Add(data)

    def AddFront(self, data):  # add front is used for adding adding in front of the queue
        self.items.append(data)
        return self.ul.Add(data)

    def RemoveRear(self):  # remove function is used removing data from rear
        return self.items.pop(0)

    def RemoveFront(self):  # remove front is used or removing data from front of the array
        return self.items.pop()

    def IsEmpty(self):  # is empty is used for empty the function
        return self.items == []

    def Size(self):  # size function is used for checking the length of the data
        print(len(self.items))

    def PrintList(self):  # print list is used for printing function
        # print(self.items)
        self.ul.Print()

    def QueueList(self):  # queue list is used for returning the items from the list
        return self.items


# stack class is made
class Stack:
    """
    stack class is created with different attribution
    """

    def __init__(self):
        self.items = []
        self.ul = LinkedList()

    def IsEmpty(self):  # is_empty is used for the return list true if empty
        return self.items == []

    def Push(self, items):  # push function is created to append the data in the stack
        self.items.append(items)
        self.ul.Add(items)

    def Pop(self):  # pop function is used for the removing a data from last index
        return self.items.pop()

    def Peek(self):  # peek is used to check the first data on the stack
        if not self.IsEmpty():
            return self.items[0:1]

    def Size(self):  # size function will give out the size of the stack
        return self.items


# hashing function is created with different parameters
class Hashing:
    """
    hashing function is created with different attributes
    """

    def __init__(self):
        self.table = [[] for _ in range(11)]

    def Hashing_Fun(self, key):  # hash is used for hashing key for inserting in the array
        # print(key%len(self.table))
        return key % len(self.table)

    def Insert(self, key):  # insert function is used for inserting data in array
        self.table[self.Hashing_Fun(key)].append(key)
        # return self.ul.add(key)
        return self.table

    def Print(self):  # print function is used for printing full table
        return self.table


# prime function is used for printing 2d array
def Prime2d():
    """
    :return: 2d array of the prime numbers are printed out
    """
    array = []  # empty array is created and data is appended
    num1 = 0
    num2 = 100

    try:  # try exception is used for the finding the error
        for data in range(10):  # loop for first 1000 numbers
            array.append(PrimeNumber(num1, num2))  # data is appended in the arry
            num1 += 100
            num2 += 100
        return array  # array is printed to check
    except AssertionError:  # if error found exception is given out
        print("plz check the index range ")
