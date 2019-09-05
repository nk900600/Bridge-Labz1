from Week1.test.test_util import PowerOf2
import unittest
import json

with open("test") as f:
    test = json.load(f)


class test_PowerOf2(unittest.TestCase):

    # method1
    def test_PowerOf2(self):
        array = ["test1", "test2", "test3", "test4", "test11"]
        for i in array:
            print(i)
            result = PowerOf2(test[0][i]["input"])
            expected = test[0][i]["output"]
            self.assertEqual(expected, result)

    # method 2
    # def test_PowerOf21(self):
    #     result = PowerOf2(test[0]["test1"]["input"])
    #     expected = test[0]["test1"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PowerOf22(self):
    #     result = PowerOf2(test[0]["test2"]["input"])
    #     expected = test[0]["test2"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PowerOf23(self):
    #     result = PowerOf2(test[0]["test3"]["input"])
    #     expected = test[0]["test3"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PowerOf24(self):
    #     result = PowerOf2(test[0]["test4"]["input"])
    #     expected = test[0]["test4"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PowerOf25(self):
    #     result = PowerOf2(test[0]["test11"]["input"])
    #     expected = test[0]["test11"]["output"]
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    test_PowerOf2()
