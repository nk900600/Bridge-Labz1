"""
 ******************************************************************************
 *  Purpose: convert decimal number to binary and swap binary and print number
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""

from Week1.Utility.utility import BinarySwap

# binary function is made for swapping nibbles


if __name__ == '__main__':

    while True:

        try:  # try is used for checking error in input
            # user input is taken
            number = int(input("number to convert into binary and swap it : "))
            # number validation is done
            if number <= 0 or number >= 10000:
                print("enter number between 0 and 10000")
                continue
            finalswap = (bin(number))[2:]
            print("binary format if this number is :  ", finalswap)
            BinarySwap(finalswap)
            break

        except ValueError:  # if error is found below code will print
            print("check the input")
