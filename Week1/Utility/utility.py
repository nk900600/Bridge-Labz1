"""
 ******************************************************************************
 *  Purpose: utils for functions programs and algorithms
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""

import datetime
import math
import sys
import numpy as np


# array function is created
def Array2d(row, col):
    """
    :param row: no of row
    :param col: no of col
    :return: 2d array
    """
    try:  # try is used for locating the error
        array = [[[np.random.randint(0, 10)] for i in range(row)] for j in range(col)]  # array is created by this
        # function
        print(array)
        return array  # array is returned
    except IndexError:
        print("index error please check ")


# CoinToss function is created to count number of heads and tails
def CoinToss(toss):
    """
    :param toss: no of flips
    :return: no of head and tails
    """
    head = 0
    tail = 0
    try:  # try is used for locating the error
        for i in range(toss):
            flip = np.random.randint(0, 2)  # random function is used for 0 and 1 output
            if flip == 0:
                head += 1
            elif flip == 1:
                tail += 1
    except IndexError:
        print("index error please check ")

    # percentage of head and tail is counted by below functions
    percentageofhead = head / toss
    percentageoftail = tail / toss
    print("total number of head and tails are ", percentageofhead, percentageoftail)


# Coupons functions used to generate random numbers
def Coupons(number):
    """
    :param number: no of coupons wants to print
    :return:
    """
    array = []  # empty array is used for storing data
    for i in range(number):
        rand = np.random.randint(10, 100)
        array.append(rand)
    # only selecting unique numbers using set.
    unique = set(array)
    print(list(unique))


# Distance is used for finding distance between 2 points
def Distance(x, y):
    """
    :param x: point 1
    :param y: point 2
    :return:  distance between 2 point
    """
    diff = math.sqrt((x ** 2 + y ** 2))
    print(diff)
    # here difference is returned
    return diff


# prime factors is used for finding factors
def PrimeFactors(number):
    """
    :param number: number is entered to find prime factors
    :return: prime factors
    """
    while number % 2 == 0:
        print(2)  # 2 prime number is printed
        number = number / 2
    # for loop is used for finding factors
    for i in range(3, int(math.sqrt(number)) + 1, 2):  # for loop is used for finding factors
        while number % i == 0:
            print(i)
            number = number / i
    # here if condition is used if number is more than 2 then print
    if number >= 2:  # condition is used if prime number is greater than 2 is printed
        print(number)


# gambler function is made for simulating gambling
def Gambler(amount):
    """
    :param amount: amount to want to play
    :return: after player final amount is returned
    """
    while True:
        try:
            play = int(input("times u want to play : "))
            # player input is taken for number of times he want to play
            if play <= 0 or play >= 11:
                print("enter between 1 and 10")
                continue
            # here input id taken on which dice number he wants to bet on
            dice = int(input("which number on the dice you want to bet : "))
            if dice <= 0 or dice >= 7:
                print("enter between 1 and 6")
                continue
            # win and loss are keeping track
            win = 0
            loss = 0
            # for loop is used for generating dice number
            for i in range(play):
                rand = np.random.rand(0, 7)
                if rand == dice:
                    amount = amount * 2
                    win += 1
                else:
                    amount = amount / 2
                    loss += 1
                # below number of win and losses are printed
                print("after round 1 total amount is ", amount)
            print("total amount won is ", amount)
            print("number of wins are ", win, "and number of losses are ", loss)
            break
        # any value error then below statement will be printed
        except ValueError:
            print("check the input ")


# harmonic function is used for calculating 1/n
def HarmonicValue(number):
    """
    :param number: number where we have to calculate harmonic function
    :return:
    """
    count = 0
    # for loop is used for calculating harmonic function
    for i in range(1, number + 1):  # for loop fot nth number
        add = 1 / i
        count += add
    # finally count is printed out
    print(count)
    return count


# leap year function is created
def LeapYear(year):
    """
    :param year: year is taken as input
    :return: year is return if its leap year
    """
    # if input is not in yyyy then this loop will interrupt
    if len(str(year)) <= 3:
        print("plz enter year in yyyy format")
    elif len(str(year)) > 4:
        print("plz enter year in yyyy format")
        return
    # if condition is used for checking leap years
    elif (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("year is a leap year")
            else:
                print("year is not a leap year")
        else:
            print("year is a leap year")
    else:
        print("year is not a leap year")


# power of 2 function is used
def PowerOf2(num):
    """
    :param num: here num is taken as input
    :return: multiplied value of 2 is given
    """
    # for loop is used multiplication
    for i in range(num):
        if i <= num:
            final = 2 ** i
        print(final)
    # final value is return
    return final


# Quad function is created
def Quad(num1, num2, num3):
    """
    :param num1: number 1 taken as input
    :param num2: number 2 taken as input
    :param num3: number 3 taken as input
    :return: after calculating quad results are returned
    """
    delta = num2 * num2 - 4 * num1 * num3
    # have to convert -ve delta to +ve ,as -ve val does not have square roots
    print(abs(delta))
    root1 = (-num2 + math.sqrt(abs(delta))) / (2 * num1)
    root2 = (-num2 - math.sqrt(abs(delta))) / (2 * num1)
    # after calculating roots output is printed
    print("root 1: ", root1)
    print("root 2 : ", root2)
    # roots are returned
    return root1, root2


# stopwatch
def StopWatch():
    """
    :return: time in sec is returned if pressed enter
    """
    start = datetime.datetime.now()
    if input("plz enter to stop the program "):
        return
    end = datetime.datetime.now()
    # prints time lapse
    print(abs(end - start))


# sum of three input are checked
def Sum(num1, num2, num3):
    """
    :param num1: input of num1 is taken
    :param num2: input of num2 is taken
    :param num3: input of num3 is taken
    :return: sum of all the input is checked is zero or not
    """
    if num1 + num2 + num3 == 0:
        print("sum is zero")
        return True
    else:
        print("sum is not zero")
        return False


# wind chill function is created to check the input
def WindChill(temp, velocity):
    """
    :param temp: temp input is taken
    :param velocity:  velocity input is taken
    :return:
    """
    power = math.pow(velocity, 0.6)
    total = 35.47 + 0.6215 * temp + (0.4275 * temp + 35.75) * power
    # total function is used for the calculation
    print(total)
    return total


# anagram function is used to compare two inputs
def Anagram(string1, string2):
    """
    :param string1: input for string1
    :param string2: input for string2
    :return: True if anagram or False is not a anagram
    """
    #  sorted pre define module is used
    if sorted(string1) == sorted(string2):
        return True
        # print("yay! its an anagram ")
    else:
        return False
        # print("uuh! its not an anagram")


# binary swapped is used for the swapping the binary number
def BinarySwap(num):
    """
    :param num: num in taken input and number is converted in binary
    :return:  swapped binary converted to decimal
    """
    # two list is created for left part of binary and right part
    left = list()
    right = list()
    try:
        for i in range(0, len(num) // 2):
            left.append(num[i])
        for i in range(len(num) // 2, len(num)):
            right.append(num[i])
    except IndexError:
        print("please check the range for the for loop")
    # now after dividing we are swapping the nibbles
    swap = "".join(left)
    swap1 = "".join(right)
    swaped = swap1 + swap
    # now we can see two prints in binary and in int
    print("after swapping , binary code is : ", swaped)
    print("final swapped number in decimal format is ", int(swaped, 2))


# Bubbles sort is used for sorting the list
def BubbleSort(llist):
    """
    :param llist: list is used and bubble sort is applied
    :return: after sorting data list is returned
    """
    # nested loops are used for  sorting
    try:  # try is used for catching the error
        for num in range(len(llist) - 1, 0, -1):
            for j in range(num):
                if llist[j] > llist[j + 1]:
                    llist[j], llist[j + 1] = llist[j + 1], llist[j]
        return llist
    except IndexError:  # error checked
        print(" check the index error ")


# day of week is used for printing the day in a week
def DayOfWeek(month, day, year):
    """
    :param month: user input is taken for month
    :param day: user input is taken for day
    :param year: user input is taken for year
    :return: day number is returned
    """
    year1 = year - (14 - month) / 12
    x = year1 + year1 / 4 - year1 / 100 + year1 / 400
    month1 = month + 12 * ((14 - month) / 12) - 2
    day1 = ((day + x + 31 * month1 / 12) % 7)
    return round(day1)
    # round function is used to round the calculation
    roundd1 = round(d1)
    if roundd1 == 0:
        print("day of the week is sunday")
    elif roundd1 == 1:
        print("day of the week is monday")
    elif roundd1 == 2:
        print("day of the week is tuesday")
    elif roundd1 == 3:
        print("day of the week is wednesday")
    elif roundd1 == 4:
        print("day of the week is thrusday")
    elif roundd1 == 5:
        print("day of the week is friday")
    else:
        print("day of the week is sat")


# insertion sort is used for the sorting the list
def InsertionSort(llist):
    """
    :param llist: unsorted list is taken as input
    :return: sorted list is return
    """
    # nested loops are used for  sorting
    try:
        for i in range(1, len(llist)):
            # for loop is used for sorting the data
            j = i - 1
            while llist[j] > llist[j + 1] and j >= 0:
                llist[j], llist[j + 1] = llist[j + 1], llist[j]
                j -= 1
        return llist
    # sorted list is returned
    except IndexError:
        print("out of index error ")


# merge sort is used for sorting list
def Merge_Sort(llist):
    """
    :param llist: unsorted list is used
    :return: sorted list is returned
    """
    MergeSort2(llist, 0, len(llist) - 1)
    # merge sort second function is called


def MergeSort2(llist, first, last):
    """
    :param llist: unsorted list is used
    :param first: first half of the list
    :param last:  second half of the list
    :return: sorted list
    """
    try:
        if first < last:  # for loop is used for sorting the data
            middle = (first + last) // 2
            MergeSort2(llist, first, middle)
            MergeSort2(llist, middle + 1, last)
            Merge(llist, first, middle, last)
    except IndexError:
        print("index error ")


# function is used for sorting
def Merge(llist, first, middle, last):
    """
    :param llist: unsorted list is used
    :param first: first half of the lsit
    :param middle: middle of the list
    :param last: last half of the list
    :return: sorted list
    """
    # list is divided in many 3 parts below
    left = llist[first:middle + 1]
    right = llist[middle + 1:last + 1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    indexi = indexj = 0

    try:  # try is used for catch the error
        for k in range(first, last + 1):  # for loop is used for sorting the data
            if left[indexi] <= right[indexj]:
                llist[k] = left[indexi]
                indexi += 1
            else:
                # Comments
                llist[k] = right[indexj]
                indexj += 1
    except IndexError:  # error is found then below function is printed
        print("check for the index error")


# monthly payments are calculated using user input
def MonthlyPayment(principle, rate, year):
    """
    :param principle: principle amount given by input
    :param rate:   rate of interest per annam
    :param year:  number of years to pay off
    :return: calulated EMI
    """
    number = 12 * year  # formula is applied and enf emi is printed out
    roi = rate / (12 * 100)
    payments = principle * roi / (1 - (1 + roi) ** (-number))
    print("monthly installments would be ", round(payments))


#  prime number are calculated using range
def PrimeNumber(num1, num2):
    """
    :param num1: num1 is taken from user
    :param num2:  num2 is taken from user
    :return:  prime number in above range is returned
    """
    prime_no = []  # empty array is created and later appended all prime numbers
    for i in range(num1, num2):  # nested loop is created and checked for the prime  numbers
        is_prime = True
        # if is prime is true then below condition will work
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            # print(i)
            prime_no.append(i)
    # print((prime_no))
    return prime_no


# palindrome function is used for checking mirror image of the input
def Palindrome(num):
    """
    :param num: input is taken
    :return: palindrome of the number
    """
    reverse = 0
    # while loop is used for recursive mode
    while num > 0:
        rem = num % 10
        reverse = (reverse * 10) + rem
        num = num // 10
    # here reverse para is returned
    return reverse


# newton method is used for the finding roots
def NewtonMethod(number, number_iters=5):
    """
    :param number: input from user to find roots
    :param number_iters: 5 is constant
    :return: roots are returned of the input
    """
    a = float(number)
    # for loop is used for the iterating through the function
    for i in range(number_iters):
        number = 0.5 * (number + a / number)
    # number is returned
    return number


# temp conversion is used for converting celsius to fahrenheit
def TemperatureConversion(celsius):
    """
    :param celsius: input is taken
    :return: converted val is returned
    """
    fahrenheit = (celsius * (9 / 5)) + 32
    print("conversion is from degree C to degree F is ", fahrenheit)
    return fahrenheit


# binary function is used for converting decimal to binary
def toBinary(number):
    """
    :param number: user input is used for converting the val
    :return: binary number is returned
    """
    binary = bin(number)
    print('The binary equivalent of 5 is:', binary)
    return binary


# vending machine is used for giving exact notes
def VendingMachine(change):
    """
    :param change: user input is taken to get the change
    :return: change is given out in minimum value
    """
    thousnads = 0  # intally all the notes are zero as programs runs notes which are suppose tobe
    fivehundred = 0  # given out will be incremented and end of the program it will print out
    fifty = 0
    hundred = 0
    tens = 0
    five = 0
    twos = 0
    onces = 0
    for notes in range(50 + 1):  # for loop is used for the calculate the total amount to be given out
        if change >= 1000:
            change -= 1000
            thousnads += 1
        elif change >= 500:
            change -= 500
            fivehundred += 1
        elif change >= 100:
            change -= 100
            hundred += 1
        elif change >= 50:
            change -= 50
            fifty += 1
        elif change >= 10:
            change -= 10
            tens += 1
        elif change >= 5:
            change -= 5
            five += 1
        elif change >= 2:
            change -= 2
            twos += 1
        elif change >= 1:
            change -= 1
            onces += 1
        elif change == 0:
            break
    # print function is used to display the exact notes to be given out
    print("no of thousands", thousnads)
    print("no of 500", fivehundred)
    print("no of 100", hundred)
    print("no of 50", fifty)
    print("no of 10", tens)
    print("no of 5", five)
    print("no of 2", twos)
    print("no of 1", onces)


# read file is used for reading the file
def ReadFile(filename):
    """
    :param filename: file name is given
    :return: file will open
    """
    with open(filename, 'r') as f:  # Open File As test.txt
        lst = f.read().split()  # Read File And Store In List
        f.close()
    return lst


# overwrite is used for the over writing file
def OverWrite(lst, filename):
    """
    :param lst: work you want to update
    :param filename:  filename where we want to update
    :return: file updated
    """
    f = open(filename, 'w')  # Open File In write mode
    for item in lst:  # Loop Through All Items in List
        f.write("%s " % item)  # Write In the File
    f.close()


# total length is used for finding total len
def Total(length):
    total = 0
    for i in range(len(length)):
        total = total + length[i]
    print(total)


# numbers are used for generating numbers in range
def Numbers(num1, num2):
    """
    :param num1: input for num1
    :param num2: input for num2
    :return: array of numbers
    """
    array = []
    for i in range(num1, num2):
        array.append(i)
    return array
