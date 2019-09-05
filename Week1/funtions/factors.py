"""
 ******************************************************************************
 *  Purpose: PrimeFactors
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import PrimeFactors

# python program to print prime factors
# function is called and end results will be prime factors of the input
if __name__ == '__main__':
    while True:
        try:  # try is used to catch any error

            prime = int(input("please enter number for finding factors :  "))
            if prime <= 0 or prime >= 1000:
                print("enter the number between 0 and 1000")
                continue
            PrimeFactors(prime)
            break

        except ValueError:
            print("check the input")
