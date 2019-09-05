from Week1.test.test_util import HarmonicValue
import unittest
import json

with open("test") as f:
    test = json.load(f)


class test_HarmonicValue1(unittest.TestCase):

    # method 1
    def test_HarmonicValue1(self):
        array = ["test1", "test2", "test3", "test4", "test5"]
        for i in array:
            print(i)
            result = HarmonicValue(test[0][i]["input"])
            expected = test[0][i]["output"]
            self.assertEqual(expected, result)

    # method 2
    # def test_HarmonicValue1(self):
    #     result = HarmonicValue(test[0]["test1"]["input"])
    #     expected = test[0]["test1"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_HarmonicValue2(self):
    #     result = HarmonicValue(test[0]["test2"]["input"])
    #     expected = test[0]["test2"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_HarmonicValue3(self):
    #     result = HarmonicValue(test[0]["test3"]["input"])
    #     expected = test[0]["test3"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_HarmonicValue4(self):
    #     result = HarmonicValue(test[0]["test4"]["input"])
    #     expected = test[0]["test4"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_HarmonicValue5(self):
    #     result = HarmonicValue(test[0]["test5"]["input"])
    #     expected = test[0]["test5"]["output"]
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    test_HarmonicValue1()
