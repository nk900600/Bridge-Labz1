"""
 ******************************************************************************
 *  Purpose: to find palindrome
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import Palindrome, PrimeNumber


# new function is used for taking input from the user
def Palindrome_Num():

    while True:
        try:    # try is used to catch any errors if any

            # user input is taken for range of numbers
            number1 = int(input("enter the first number of a range: "))
            if number1 <= 10 or number1 >= 10000:
                print("enter the number between 10 and 10000")
                continue
            number2 = int(input("enter the second number of a range : "))
            if number2 <= number1 or number2 >= 10000:
                print("second number should be greater than first number")
                continue

            prime=PrimeNumber(number1, number2)
            palindromnum=[]      # empty array is created where numbers are added and printed

            for i in range(len(prime)):      # for loop is used for the comparing two number to check palindrome
                numstr = list(str(prime[i]))
                for j in range(len(prime)):
                    numstr1 = list(str(prime[j]))
                    if numstr != numstr1[::-1]:    # if condition is used for checking palindrome number
                        pass
                    else:
                        palindromnum.append(prime[j])    # if number is palindrome then number will be appended in
                        # the list
            print((set(palindromnum)))   # finally number will be printed
            break

        except ValueError:    # if input error then below code will be printed
            print("check the user input")


"""
main function is called 
"""
if __name__ == '__main__':

    Palindrome_Num()