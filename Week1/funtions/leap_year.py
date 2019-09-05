"""
 ******************************************************************************
 *  Purpose: to find Leap Year
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import LeapYear

# leap-year function is created
# function is called
if __name__ == '__main__':
    while True:

        try:  # try is used for catching any error
            year = int(input("enter year in yyyy format  : "))
            if year <= 1000 or year >= 10000:
                print("enter year again")
                continue
            LeapYear(year)
            break
        except ValueError:  # value error
            print("check the input")
