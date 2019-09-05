
"""
 ******************************************************************************
 *  Purpose: binary Conversion
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import VendingMachine


# function is created where minimum notes will given out
if __name__ == '__main__':
    while True:
        # input is taken and is passed on to the machine function
        try:

            change = int(input(" plz enter the amount :"))    # user input is taken
            if change <= 0 or change >= 10000:
                print("enter between 0 and 10000 ")
                continue
            VendingMachine(change)
            break
        except ValueError:
            print("check the input")


