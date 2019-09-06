from Week2.ordered_list import OrderedList
from Week2.node_linked_and_sorted import LinkedList
import unittest


class test_orderedlist(unittest.TestCase):  # test case is created with unittest

    def test_orderedlist(self):  # function is made

        llist = LinkedList()  # linked list is called
        order = OrderedList()  # results is stored in var
        self.assertEqual(order, llist.Size())  # here data is checked


if __name__ == '__main__':
    test_orderedlist()
