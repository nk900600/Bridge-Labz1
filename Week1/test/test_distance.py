from Week1.test.test_util import Distance
import unittest
import json

with open("test") as f:
    test = json.load(f)


class test_Distance1(unittest.TestCase):

    # method 1
    def test_Distance1(self):
        array = ["test1", "test2", "test3", "test4", "test6"]
        for i in array:
            print(i)
            result = Distance(test[0][i]["input"],test[0][i]["input"])
            expected = test[0][i]["output"]
            self.assertEqual(expected, result)

    #  method 2
    # def test_Distance1(self):
    #     result = Distance(test[0]["test1"]["input"], test[0]["test1"]["input"])
    #     expected = test[0]["test1"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_Distance2(self):
    #     result = Distance(test[0]["test2"]["input"], test[0]["test2"]["input"])
    #     expected = test[0]["test2"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_Distance3(self):
    #     result = Distance(test[0]["test3"]["input"], test[0]["test4"]["input"])
    #     expected = test[0]["test3"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_Distance4(self):
    #     result = Distance(test[0]["test4"]["input"], test[0]["test4"]["input"])
    #     expected = test[0]["test4"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_Distance5(self):
    #     result = Distance(test[0]["test6"]["input"], test[0]["test6"]["input"])
    #     expected = test[0]["test6"]["output"]
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    test_Distance1()
