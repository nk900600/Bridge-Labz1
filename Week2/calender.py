"""
 ******************************************************************************
 *  Purpose: Calender printing
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import DayOfWeek


# calender function is used for printing out calender
def Calender(month, year):  # calender function is created and will print 2d calender

    array = [["" for i in range(0, 7)] for j in range(0, 7)]  # empty array is created
    day = ["s", "m", "t", "w", "th", "f", "s"]  # days are added to the top of array index 0
    daysinmonth = [0, 31, 28, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31]  # number of days in the months are printed
    array[0] = day  # replacing array 0 with day

    startday = DayOfWeek(month, 1, year)

    try:  # try is used for locating the error
        for days in range(startday):  # for loop is used to space out the array till the start of the month
            array[1][days] = ""
        monthindex = 1
        start = startday  # here we have given our start day as one

        for j in range(1, daysinmonth[month] + 1):  # for loop is used for adding numbers in the array
            (array[monthindex][start]) = j
            start += 1
            if (j + startday) % 7 == 0:  # if condition is used moving to next array
                monthindex += 1
                start = 0

        return array  # 2d array is return where all the numbers can be seen printed out

    except ValueError:  # value error can be detected
        print("please check the input value ")

# main function is created
if __name__ == '__main__':
    while True:
        try:
            # input for the month and year is taken from the user
            month = int(input("which month's calender u wish to see in MM format :"))
            if month <= 0 or month >= 13:
                print("enter between 0 and 13")
                continue
            year = int(input("for which year YYYY format"))
            if year <= 1000 or year >= 3000:
                print("enter between 1000 and 3000")
                continue
            array = Calender(month, year)
    # for loop is used for printing the calender
            for i in range(0, 7):
                for j in range(0, 7):
                    print("{:>2}".format(array[i][j]), end="  ")
                print()

            break
        except ValueError:
            print("check the input")
