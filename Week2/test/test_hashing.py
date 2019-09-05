from Week2.node_linked_and_sorted import LinkedList
from Week2.hashing_file import HashingFile
import unittest

"""

test class is created to check the program using unittest

"""


class test_hashingfile(unittest.TestCase):  # test class is created using unittest

    def test_hashingfile(self):     # this function is created to check the program

        llist = LinkedList()    # linked list
        file = HashingFile()    # here program results are stored in the var
        self.assertEqual(file, llist.Size())    # now file and var is compared


"""
main function is created
"""
if __name__ == '__main__':
    test_hashingfile()
