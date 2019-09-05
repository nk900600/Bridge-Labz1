from Week1.test.test_util import BinarySwap
import unittest
import json

with open("test") as f:
    test = json.load(f)


class test_BinarySwap1(unittest.TestCase):

    # method 1
    def test_BinarySwap1(self):
        array = ["test1", "test2", "test3", "test4"]
        for i in array:
            print(i)
            result = BinarySwap(test[0][i]["input"])
            expected = test[0][i]["output"]
            self.assertEqual(expected, result)

    #  method 2
    # def test_BinarySwap11(self):
    #     result = BinarySwap(test[0]["test1"]["input"])
    #     expected = test[0]["test1"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_BinarySwap12(self):
    #     result = BinarySwap(test[0]["test2"]["input"])
    #     expected = test[0]["test2"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_BinarySwap13(self):
    #     result = BinarySwap(test[0]["test3"]["input"])
    #     expected = test[0]["test3"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_BinarySwap14(self):
    #     result = BinarySwap(test[0]["test4"]["input"])
    #     expected = test[0]["test4"]["output"]
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    test_BinarySwap1()
