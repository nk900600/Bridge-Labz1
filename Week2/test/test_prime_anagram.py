from Week2.prime_number_anagram import PrimeAnagram
import unittest


class test_primeanagram(unittest.TestCase):  # function is created by unittest

    def test_primeanagram(self):
        prime = PrimeAnagram()  # here programs output is stored
        self.assertEqual(prime,
                         [31, 41, 43, 53, 61, 71, 73, 83, 97, 131, 151, 163, 173, 181, 191, 193, 197, 211, 241, 251,
                          263, 271, 281, 283, 293, 311, 313, 317, 331, 353, 373, 383, 397, 401, 419, 421, 431, 433, 439,
                          443, 461, 463, 487, 491, 503, 521, 523, 541, 547, 563, 571, 587, 593, 601, 613, 617, 619, 631,
                          641, 643, 647, 653, 659, 661, 673, 683, 691, 701, 719, 727, 733, 739, 743, 751, 757, 761, 769,
                          773, 787, 797, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
                          919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])


if __name__ == '__main__':
    test_primeanagram()
