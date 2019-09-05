"""
 ******************************************************************************
 *  Purpose: calculate HarmonicValue
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import HarmonicValue

# input is given and function is called
if __name__ == '__main__':
    while True:

        try:  # try is used for catching any error

            number = int(input("enter the number to find its harmonic value : "))
            if number <= 0 or number >= 1000:
                print("enter between 0 and 1000")
                continue
            HarmonicValue(number)
            break

        except ValueError:
            print("check the input")
