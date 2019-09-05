from Week2.node_linked_and_sorted import LinkedList
from Week2.calendar_using_linked_list import Calender_Using_Linked_List
import unittest
"""

test class is created to check the program using unittest

"""


class test_calender_using_linked_list(unittest.TestCase):    # test class is used for unittest

    def test_calender_using_linked_list(self):    # test function is created

        llist=LinkedList()     # linked list is called and object is created
        calen = Calender_Using_Linked_List()   # here results are stored in var
        self.assertEqual(calen,llist.Size())   # validation is done by comparing with answer

"""
main function 
"""
if __name__ == '__main__':
    test_calender_using_linked_list()
