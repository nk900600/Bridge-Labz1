from Week2.palindrome_checker import Palindrome
from Week2.util import Queue1
import unittest



class test_palindrome(unittest.TestCase):  # test case is created using unittest

    def test_palindrome(self):
        q = Queue1()               # queue function is created
        palind = Palindrome("nik")
        self.assertEqual(palind, q.Size())    # here we will compare the error


if __name__ == '__main__':
    test_palindrome()
