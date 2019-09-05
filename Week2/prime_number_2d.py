"""
 ******************************************************************************
 *  Purpose: to print prime 2d
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import PrimeNumber


# prime function is used for printing 2d array
def Prime2d():
    """
    :return: 2d array of the prime numbers are printed out
    """
    array = []  # empty array is created and data is appended
    num1 = 0
    num2 = 100
    try:  # try exception is used for the finding the error
        for data in range(10):  # loop for first 1000 numbers
            array.append(PrimeNumber(num1, num2))  # data is appended in the arry
            num1 += 100
            num2 += 100
        return array  # array is printed to check
    except AssertionError:  # if error found exception is given out
        print("plz check the index range ")


# main function is created
if __name__ == '__main__':
    print(Prime2d())
