"""
 ******************************************************************************
 *  Purpose: to find power of 2
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import PowerOf2

# function is called
if __name__ == '__main__':
    while True:
        try:  # try is used for catching any error

            userinput = int(input("enter num : "))
            if userinput <= 0 or userinput >= 100:
                print("enter between 0 and 100")
                continue
            PowerOf2(userinput)
            break
        except ValueError:
            print("check the user input")
