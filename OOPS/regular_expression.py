"""
 ******************************************************************************
 *  Purpose:  regex_replace
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
import re
import datetime


# regex function is used for replacing the numbers
def Regex_Replace():
    while True:
        try:  # try method is used to catch the input error

            # user input is taken for the below details
            name = input("enter your name :")  # input for the user
            if name.isalpha() is not True:
                print(" enter vaild name ")
                continue
            fullname = input("enter your full name please")
            mobile_number = int(input("please enter your mobile number in 91xxxxxxxxxx format"))
            if mobile_number >= 920000000000 or mobile_number <= 915999999999:
                print("enter vaild mobile number")
            now = datetime.datetime.now()
            date = now.strftime("%d/%m/%Y")
            # here number validation is done for number
            # data from where file will be replaced
            file = """Read in the following message: Hello <<name>>, We have your full name as <<full name>> in our system. 
                    your contact number is 91­xxxxxxxxxx.Please,let us know in case of any
                     clarification Thank you BridgeLabz XX/XX/XXXX """

            # regex method is used for the checking the pattern from the data

            namesub = re.compile("<<\w+>>")  # pattern for name
            fullnamesub = re.compile("<<\w+.\w+>>")  # pattern for full name
            numersub = re.compile("\d+.\w+")  # pattern for number.
            datesub = re.compile("\w+/\w+/\w+")

            # here all the pattern catch by the re is substitute in the data

            file = re.sub(namesub, name.upper(), file)
            file = re.sub(fullnamesub, fullname.upper(), file)
            file = re.sub(numersub, str(mobile_number), file)
            file = re.sub(datesub, date, file)

            # now the replaced data is printed
            print(file)
            break
        except:
            print("check the input")


# main function is created
if __name__ == '__main__':
    Regex_Replace()  # function is called
