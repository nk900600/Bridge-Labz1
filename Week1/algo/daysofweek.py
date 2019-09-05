"""
 ******************************************************************************
 *  Purpose: to find day of the week
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import DayOfWeek

# below function will give out the day of the week in numbers
if __name__ == '__main__':
    while True:

        try:  # try is used for catching any error if any
            # below we have taken user input
            month = int(input("enter month in mm format : "))
            if len(str(month)) >= 3 or month >= 13:
                print(" please the check input")
                continue

            year = int(input("enter year in yyyy format : "))
            if len(str(year)) >= 5 or year <= 1000:
                print(" please the check input")
                continue

            day = int(input("enter day in dd format : "))
            if len(str(day)) >= 3 or day >= 32:
                print(" please the check input")
                continue

            # below day is printed in number
            print(" today's day is ", DayOfWeek(month, year, day))
            break

        except ValueError:
            print("check the user input")
