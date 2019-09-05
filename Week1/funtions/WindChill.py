"""
 ******************************************************************************
 *  Purpose: sum of input
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import WindChill

# this program is created toc calculate wind chills by user input
if __name__ == '__main__':
    while True:
        try:  # try is used for catching any error

            temp = int(input("enter temp below 50 in fahrenheit : "))
            if temp >= 51:
                print("enter between 50 and 1000")
                continue
            velocity = int(input("enter velocity in range of 3m/s and  120m/s : "))
            if velocity <= 4 or velocity >= 121:
                print("enter number between 3 and 120 ")
                continue
            WindChill(temp, velocity)
            break

        except ValueError:  # if error is found then below statement will be printed
            print("check the input")
