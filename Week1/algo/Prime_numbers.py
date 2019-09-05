"""
 ******************************************************************************
 *  Purpose: to find PrimeNumber
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import PrimeNumber


# prime number function is called from the utility and prime number will be printed in that range
if __name__ == '__main__':
    while True:
        try:    # try function is used for the checking user input

            number1 = int(input("enter the first number of a range: "))
            if number1 <= 0 or number1 >= 10000:
                print("enter the number between 1 and 10000")
                continue
            number2 = int(input("enter the second number of a range : "))
            if number2 <= number1 or number2 >= 10000:
                print("second number should be greater than first number")
                continue

            print(PrimeNumber(number1, number2))
            print("total length of the prime numbers in range is ", len((PrimeNumber(number1,number2))))
            break

        except ValueError:  # if user input error is found and below statement is printed
            print("check the user input")


