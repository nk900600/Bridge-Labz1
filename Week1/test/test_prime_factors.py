from Week1.test.test_util import PrimeFactors
import unittest
import json

with open("test") as f:
    test = json.load(f)


class test_PrimeFactors(unittest.TestCase):

    # method 1
    def test_PrimeFactors(self):
        array = ["test1", "test2", "test3", "test4", "test12"]
        for i in array:
            print(i)
            result = PrimeFactors(test[0][i]["input"])
            expected = test[0][i]["output"]
            self.assertEqual(expected, result)

    # method 2
    # def test_PrimeFactors1(self):
    #     result = PrimeFactors(test[0]["test1"]["input"])
    #     expected = test[0]["test1"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PrimeFactors2(self):
    #     result = PrimeFactors(test[0]["test2"]["input"])
    #     expected = test[0]["test2"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PrimeFactors3(self):
    #     result = PrimeFactors(test[0]["test3"]["input"])
    #     expected = test[0]["test3"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PrimeFactors4(self):
    #     result = PrimeFactors(test[0]["test4"]["input"])
    #     expected = test[0]["test4"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PrimeFactors5(self):
    #     result = PrimeFactors(test[0]["test12"]["input"])
    #     expected = test[0]["test12"]["output"]
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    test_PrimeFactors()
