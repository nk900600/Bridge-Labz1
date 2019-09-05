"""
 ******************************************************************************
 *  Purpose: to find palindrome
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week2.util import Queue1


# class is called and below sample id printed to check queue class
# palindrome function is created
def Palindrome(string1):
    while True:
        q = Queue1()
        string1_list = list(string1)  # converting string into list for checking with queue list
        print(string1_list)  # printing list to double check
        # for loop is used to iterate the function and add items to rear of the list
        try:  # try catch function is use for the error if any

            for i in range(len(string1_list)):
                q.AddRear(string1_list[i])

            q.PrintList()  # list is printed to check
            # print(q.queuelist())

            if q.QueueList() == string1_list:  # this if condition is used to compare both list  and give out results
                print("its a palindrome")
            else:
                print("its not a palindrome")

            break
        except ValueError:
            print("check the input data")


# main function is created to call the function
if __name__ == '__main__':
    while True:
        try:    # looping function is used for looping through the input is wring
            user = input("enter a word : ")  # user will enter any word
            if user.isalpha() is not True:
                print("check input")
                continue
            Palindrome(user)  # function is called here
            break
        except ValueError:
            print("check input")