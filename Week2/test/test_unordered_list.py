from Week2.unordered_list import UnorderedlList
from Week2.node_linked_and_sorted import LinkedList
import unittest

"""

test class is created to check the program using unittest

"""


class test_unorderedlist(unittest.TestCase):  # test case is created by unittest

    def test_unorderedlist(self):
        llist = LinkedList()
        unorder = UnorderedlList()
        self.assertEqual(unorder, llist.Size())  # here data is cross verify


if __name__ == '__main__':
    test_unorderedlist()
