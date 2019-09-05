from Week1.test.test_util import InsertionSort
import unittest
import json

with open("test") as f:
    test = json.load(f)


class test_InsertionSort(unittest.TestCase):

    def test_InsertionSort(self):
        array = ["test1", "test2", "test3", "test4", "test7"]
        for i in array:
            print(i)
            result = InsertionSort(test[0][i]["input"])
            expected = test[0][i]["output"]
            self.assertEqual(expected, result)


if __name__ == '__main__':
    test_InsertionSort()
