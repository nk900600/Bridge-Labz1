"""
 ******************************************************************************
 *  Purpose: simulates gambling
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import Gambler

# before calling function taking input for $$money$$
if __name__ == '__main__':
    while True:
        try:  # try is used for catching any error

            amount = int(input("amount :"))
            if amount <= 0 or amount >= 1000:
                print("enter the number between 0 and 1000")
                continue
            Gambler(amount)
            break

        except ValueError:
            print("check the input")
