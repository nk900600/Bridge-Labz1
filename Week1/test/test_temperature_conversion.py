from Week1.test.test_util import TemperatureConversion
import unittest
import json

with open("test") as f:
    test = json.load(f)


class test_TemperatureConversion(unittest.TestCase):

    # method 1
    def test_TemperatureConversion(self):
        array = ["test1", "test2", "test3", "test4", "test10"]
        for i in array:
            print(i)
            result = TemperatureConversion(test[0][i]["input"])
            expected = test[0][i]["output"]
            self.assertEqual(expected, result)

    # method 2
    # def test_TemperatureConversion1(self):
    #     result = TemperatureConversion(test[0]["test1"]["input"])
    #     expected = test[0]["test1"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_TemperatureConversion2(self):
    #     result = TemperatureConversion(test[0]["test2"]["input"])
    #     expected = test[0]["test2"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_TemperatureConversion3(self):
    #     result = TemperatureConversion(test[0]["test3"]["input"])
    #     expected = test[0]["test3"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_TemperatureConversion4(self):
    #     result = TemperatureConversion(test[0]["test4"]["input"])
    #     expected = test[0]["test4"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_TemperatureConversion5(self):
    #     result = TemperatureConversion(test[0]["test10"]["input"])
    #     expected = test[0]["test10"]["output"]
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    test_TemperatureConversion()
