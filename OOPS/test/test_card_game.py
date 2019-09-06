from OOPS.test_oops_util import CardGame
import unittest
import json


with open("/home/admin1/PycharmProjects/bridge_labz/Week1/test/test") as f:
    test = json.load(f)


class test_CardGame(unittest.TestCase):

    # method 1
    def test_CardGame(self):
        array = ["test1", "test2", "test3", "test4"]
        for i in array:
            print(i)
            result = CardGame.Distribute(test[0][i]["input"],test[0][i]["input"])
            expected = test[0][i]["output"]
            self.assertEqual(expected, result)

    #  method 2
    # def test_CardGame1(self):
    #     result = CardGame.Distribute(test[0]["test1"]["input"], test[0]["test1"]["input"])
    #     expected = test[0]["test1"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_CardGame2(self):
    #     result = CardGame.Distribute(test[0]["test2"]["input"], test[0]["test2"]["input"])
    #     expected = test[0]["test2"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_CardGame3(self):
    #     result = CardGame.Distribute(test[0]["test3"]["input"], test[0]["test3"]["input"])
    #     expected = test[0]["test3"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_CardGame4(self):
    #     result = CardGame.Distribute(test[0]["test4"]["input"], test[0]["test4"]["input"])
    #     expected = test[0]["test4"]["output"]
    #     self.assertEqual(expected, result)
    #


if __name__ == '__main__':
    test_CardGame()
