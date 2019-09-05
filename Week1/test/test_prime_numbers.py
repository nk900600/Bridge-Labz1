from Week1.test.test_util import PrimeNumber
import unittest
import json

with open("test") as f:
    test = json.load(f)


class test_PrimeNumber(unittest.TestCase):

    # method 1
    def test_PrimeNumber(self):
        array = ["test1", "test2", "test3", "test4", "test8"]
        for i in array:
            print(i)
            result = PrimeNumber(test[0][i]["input"], test[0][i]["input1"])
            expected = test[0][i]["output"]
            self.assertEqual(expected, result)

    # method 2
    # def test_PrimeNumber1(self):
    #     result = PrimeNumber(test[0]["test1"]["input"],test[0]["test1"]["input1"])
    #     expected = test[0]["test1"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PrimeNumber2(self):
    #     result = PrimeNumber(test[0]["test2"]["input"], test[0]["test2"]["input1"])
    #     expected = test[0]["test2"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PrimeNumber3(self):
    #     result = PrimeNumber(test[0]["test3"]["input"], test[0]["test3"]["input1"])
    #     expected = test[0]["test3"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PrimeNumber4(self):
    #     result = PrimeNumber(test[0]["test4"]["input"],test[0]["test4"]["input1"])
    #     expected = test[0]["test4"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_PrimeNumber5(self):
    #     result = PrimeNumber(test[0]["test8"]["input"],test[0]["test8"]["input1"])
    #     expected = test[0]["test8"]["output"]
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    test_PrimeNumber()
