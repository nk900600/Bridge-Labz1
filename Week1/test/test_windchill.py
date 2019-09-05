from Week1.test.test_util import WindChill
import unittest
import json

with open("test") as f:
    test = json.load(f)


class test_WindChill(unittest.TestCase):

    # method 1
    def test_WindChill(self):
        array = ["test1", "test2", "test3", "test4", "test9"]
        for i in array:
            print(i)
            result = WindChill(test[0][i]["input"],test[0][i]["input1"])
            expected = test[0][i]["output"]
            self.assertEqual(expected, result)

    # method 2
    # def test_WindChill1(self):
    #     result = WindChill(test[0]["test1"]["input"], test[0]["test1"]["input1"])
    #     expected = test[0]["test1"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_WindChill2(self):
    #     result = WindChill(test[0]["test2"]["input"], test[0]["test2"]["input1"])
    #     expected = test[0]["test2"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_WindChill3(self):
    #     result = WindChill(test[0]["test3"]["input"], test[0]["test3"]["input1"])
    #     expected = test[0]["test3"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_WindChill4(self):
    #     result = WindChill(test[0]["test4"]["input"], test[0]["test4"]["input1"])
    #     expected = test[0]["test4"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_WindChill5(self):
    #     result = WindChill(test[0]["test9"]["input"], test[0]["test9"]["input1"])
    #     expected = test[0]["test9"]["output"]
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    test_WindChill()
