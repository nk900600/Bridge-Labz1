"""
 ******************************************************************************
 *  Purpose: to print Prime Anagram
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import Anagram
from Week2.prime_number_2d import Prime2d


# prime anagram is used for printing data
def PrimeAnagram():

    z = Prime2d()
    final = []
    try:      # try exception is used for the finding the error
        for items in z[:]:  # as its is 2d array we have to convert it single array
            for data in items:   # after that we have iterated
                for j in range(data):  # we have used nested loop
                    if Anagram(str(data), str(j)):  # now anagram function is  called and data in items is printed
                        final.append(data)

    except IndexError:  # out of range error is used
        print(" it is out of range ")

    arrt = list(set(final))  # set function is used for removing duplicates
    arrt.sort()
    return arrt


# main function is created
if __name__ == '__main__':
    print(PrimeAnagram())





