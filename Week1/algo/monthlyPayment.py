"""
 ******************************************************************************
 *  Purpose: to find MonthlyPayment
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import MonthlyPayment

# here EMI is calculated by taking user input
if __name__ == '__main__':

    while True:
        try:  # try is used for catching user input values

            Principle = int(input("principal loan amount : "))
            if Principle <= 0 or Principle >= 10000000:
                print("check the principle input ")
                continue
            Rate_of_interest = float(input("Rate of interest compounded monthly : "))
            if Rate_of_interest <= 0 or Rate_of_interest >= 101:
                print("check the rate of interest input ")
                continue
            Year = int(input("years to pay off : "))
            if Year >= 100 or len(str(Year)) >= 5:
                print("check the year input it should be less than 101 ")
                continue
            MonthlyPayment(Principle, Rate_of_interest, Year)
            break

        except ValueError:  # if user input any thing apart from number then below statement will print
            print("check the ValueError")
