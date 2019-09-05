"""
 ******************************************************************************
 *  Purpose: Temperature Conversion
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import TemperatureConversion

# temperature conversion is used in below code
if __name__ == '__main__':
    while True:
        try:  # try is used for checking for error if any

            user = int(input("enter temp in degree Celsius : "))
            if user <= 0 or user >= 10000:
                print("enter between 0 and 10000 ")
                continue

            TemperatureConversion(user)
            break

        except ValueError:  # if error is found below statement is
            print(" please check the input ")
