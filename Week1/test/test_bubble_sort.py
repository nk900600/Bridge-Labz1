from Week1.test.test_util import BubbleSort
import unittest
import json

with open("test") as f:
    test = json.load(f)


class test_bubblesort(unittest.TestCase):

    # method 1
    def test_bubblesort(self):
        array = ["test1", "test2", "test3", "test4", "test7"]
        for i in array:
            print(i)
            result = BubbleSort(test[0][i]["input"])
            expected = test[0][i]["output"]
            self.assertEqual(expected, result)

    # method 2
    # def test_bubblesort1(self):
    #     result = BubbleSort(test[0]["test1"]["input"])
    #     expected = test[0]["test1"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_bubblesort2(self):
    #     result = BubbleSort(test[0]["test2"]["input"])
    #     expected = test[0]["test2"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_bubblesort3(self):
    #     result = BubbleSort(test[0]["test3"]["input"])
    #     expected = test[0]["test3"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_bubblesort4(self):
    #     result = BubbleSort(test[0]["test4"]["input"])
    #     expected = test[0]["test4"]["output"]
    #     self.assertEqual(expected, result)
    #
    # def test_bubblesort5(self):
    #     result = BubbleSort(test[0]["test7"]["input"])
    #     expected = test[0]["test7"]["output"]
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    test_bubblesort()
