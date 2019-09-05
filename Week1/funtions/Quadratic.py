"""
 ******************************************************************************
 *  Purpose: to find Quadratic equation
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import Quad

if __name__ == '__main__':
    while True:
        try:  # try is used for catching any error

            num1 = int(input("enter number 1 :"))
            if num1 <= 0 or num1 >= 1000:
                print("enter between 0 and 1000")
                continue
            num2 = int(input("enter number 2 :"))
            if num2 <= 0 or num2 >= 1000:
                print("enter between 0 and 1000")
                continue
            num3 = int(input("enter number 3 :"))
            if num3 <= 0 or num3 >= 1000:
                print("enter between 0 and 1000")
                continue
            Quad(num1, num2, num3)
            break

        except ValueError:
            print("check user input")
