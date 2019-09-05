from Week2.prime_anagram_reversed import Anagram_Reversed
from Week2.node_linked_and_sorted import LinkedList
import unittest
"""

test class is created to check the program using unittest

"""

class test_anagram_queue(unittest.TestCase):   # test class is made using unittest

    def test_anagram_queue(self):   # test function made for checking the program

        llist=LinkedList()    # linked list is imported
        ana = Anagram_Reversed()    # here function is stored in var
        self.assertEqual(ana,llist.Size())    # here we validated the program


"""
main function is made and below function is called 
"""

if __name__ == '__main__':
    test_anagram_queue()
