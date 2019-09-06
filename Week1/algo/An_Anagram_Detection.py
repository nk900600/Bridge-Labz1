"""
 ******************************************************************************
 *  Purpose: Determines whether anagram or not
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""

from Week1.Utility.utility import Anagram

# here anagram function is used for matching two input

if __name__ == '__main__':

    while True:
        try:  # try function is used for finding any error
            # input is taken from user
            word1 = input("plz enter any word : ")
            # input validation is done
            if word1.isalpha() is not True:
                print("check the input ")
                continue
            word2 = input("plz enter another word for anagram detection : ")
            if word2.isalpha() is not True:
                print("check the input ")
                continue
            print(Anagram(word1, word2))  # anagram function is called from utility
            break

        except ValueError:  # if value error then below statement will print
            print("check the input")
