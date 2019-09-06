from Week2.prime_anagram_queue import Anagram_Queue
from Week2.util import Queue1
import unittest


class test_anagram_queue(unittest.TestCase):  # test class is created with unittest

    def test_anagram_queue(self):  # test_ function is made

        q = Queue1()      # queue is imported
        ana = Anagram_Queue()    # here function is stored in var
        self.assertEqual(ana, q.Size())   # here we validated the program


if __name__ == '__main__':
    test_anagram_queue()
