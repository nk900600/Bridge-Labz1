"""
 ******************************************************************************
 *  Purpose: to find square root
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import NewtonMethod

# function is created for newton number
if __name__ == '__main__':
    while True:

        try:  # try is used for catching input error

            num = int(input("enter the number to find the its root :"))
            if num <= 0 or num >= 10000:
                print("enter between 1 to 10000")
                continue
            print(NewtonMethod(num))
            break

        except ValueError:  # to check input
            print("check the input")
