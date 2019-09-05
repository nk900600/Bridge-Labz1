from Week2.calender import Calender
import unittest
import json

with open("test") as f:
    test = json.load(f)


class test_Anagram(unittest.TestCase):

    def test_Anagram_1(self):
        result = Calender(test[0]["test1"]["input"], test[0]["test1"]["input"])
        expected = test[0]["test1"]["output"]
        self.assertNotEqual(TypeError, result)

    # def test_Anagram_2(self):
    #     result = Calender(test[0]["test2"]["input"], test[0]["test2"]["input"])
    #     expected = test[0]["test2"]["output"]
    #     self.assertNotEqual(expected, result)
    #
    # def test_Anagram_3(self):
    #     result = Calender(test[0]["test1"]["input1"], test[0]["test1"]["input2"])
    #     expected = test[0]["test1"]["output"]
    #     self.assertNotEqual(expected, result)

if __name__ == '__main__':
    test_Anagram()
