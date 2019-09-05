"""
 ******************************************************************************
 *  Purpose: distance calculators
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import Distance

# by importing math for sqrt function
if __name__ == '__main__':
    while True:
        try:  # try is used for catching errors

            x = int(input("enter num 1 : "))
            if x <= 0 or x >= 1000:
                print("enter the number between 0 and 1000")
                continue
            y = int(input("enter num 2 : "))
            if y <= 0 or y >= 1000:
                print("enter the number between 0 and 1000")
                continue

            # function is called
            Distance(x, y)
            break
        except ValueError:  # if error is caught then below statement will be printed
            print("check the input ")
