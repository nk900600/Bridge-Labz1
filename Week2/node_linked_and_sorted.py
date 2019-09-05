"""
 ******************************************************************************
 *  Purpose: util for linked list class
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import BubbleSort


class Node:
    def __init__(self, data):  # data is initialized
        self.data = data
        self.next = None


# linked list class is made
class LinkedList:
    """
    linked list class is made with different attributes
    """

    def __init__(self):  # this in initialization
        self.head = None

    def Add_To_Start(self, data):  # here data is added to start of the list
        """
        :param data: data is input what we can add to the list
        :return: linked list
        """
        new = Node(data)
        new.next = self.head
        self.head = new

    def Add(self, data):  # data is added to the linked list
        """
        :param data: data is input what we can add to the list
        :return: linked list
        """
        new = Node(data)
        curr = self.head
        if curr is None:  # if list is empty then we will add data to the start
            self.Add_To_Start(data)
        else:
            while curr.next is not None:  # while loop is used for the curr to curr.next
                curr = curr.next
            curr.next = new

    def PrintCalendar(self):  # this function is used for printing calender
        """
        :return: calender in linked list
        """
        curr = self.head
        g = 0
        for i in range(0, 7):  # for loop is used to printing calender
            while curr is not None:  # while loop is used for printing calendar
                g += 1
                print("{:>2}".format(curr.data), end="  ")
                curr = curr.next
                if g == 7:
                    g = 0
                    break
            print()

    def Print(self):  # print is used for printing out the data in the linked list
        """
        :return:  prints out the data in linked list
        """
        curr = self.head
        while curr is not None:  # while loop is used printing data
            print(curr.data, end=" ")
            curr = curr.next

    def Remove(self, data):  # remove function is used for removing the data from the linked list
        """
        :param data: particular data is removed after user input
        :return: data is returned
        """
        global prev, newlink
        curr = self.head
        if curr.data == data:  # if data at the head then head wil be replaced with next node
            self.Delete_To_Start()
        elif curr is None:  # if head is none then below print statement
            print("no list found")
        else:
            newlink = None
            prev = None
            while curr.next is not None:  # while loop is used for checking next node and then replacing
                if curr.data == data:
                    newlink = curr.next
                    break
                else:
                    prev = curr
                    curr = curr.next
            prev.next = newlink  # new address is saved and replaced with prev address

    def Delete_To_Start(self):
        """
        :return:  will delete head nodes data
        """
        self.head = self.head.next  # delete function is used to replace data with the net node

    def Delete_At_End(self):
        """
        :return:  will delete last nodes data
        """
        curr = self.head
        if curr is None:  # if list is empty the below statement is printed
            print("list is empty")
        else:
            prev = None
            while curr.next is not None:  # while loop is used for the replacing the address of the node
                prev = curr
                curr = curr.next
            prev.next = None

    def Add_At_Position(self, position, data):
        """
        :param position: position at which data user wants to delete
        :param data: data user wants to delete
        :return: data will be deleted
        """
        new = Node(data)
        curr = self.head
        if curr is None:  # if list is empty then below statement wll be printed
            self.Add_To_Start(data)
        else:
            for position in range(position - 1):  # for loop is used to check the address and replace the data
                curr = curr.next
            prev = curr.next
            curr.next = new
            new.next = prev

    def Delete_At_Position(self, position):
        """
        :param position: will delete the data at the position
        :return: de linked data
        """
        curr = self.head
        if curr is None:  # if list is empty then below statement will printed
            print("list is empty")
        else:
            for position in range(position - 1):  # for loop is used for checking the address and deleting the data
                curr = curr.next
            prev = curr.next.next
            curr.next = prev

    def Search(self, data):
        """
        :param data: will take input from the user and check if data exist in the linked list
        :return: will return true or false
        """
        curr = self.head
        if curr is None:  # if list is empty then delete
            print("list is empty")
        else:
           while curr.next is not None:  # while loop is used for finding address
                if curr.next.data == data:
                    return True
                curr = curr.next

    def sortlist(self):
        """
        :return: sorted list will be returned
        """
        arr = []
        curr = self.head
        while curr is not None:  # while loop is used for the appending the data
            arr.append(curr.data)
            curr = curr.next
        sortedlist = BubbleSort(arr)  # sorting the data from bubble
        llist = LinkedList()
        for item in sortedlist:  # then data is added to the linked list
            llist.Add(item)
        llist.Print()

    def Size(self):
        """
        :return: will return size of the linked list
        """
        curr = self.head
        count = 0
        while curr is not None:  # while loop is used for counting data in linked list
            curr = curr.next
            count += 1
        print(count)

    def data(self):
        return self.data()

