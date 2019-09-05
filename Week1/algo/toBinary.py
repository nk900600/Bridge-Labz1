"""
 ******************************************************************************
 *  Purpose: binary Conversion
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import toBinary

# binary function is created for conversion
if __name__ == '__main__':
    while True:
        try:  # user input is used
            user = int(input("number plz : "))
            if user <= 0 or user >= 10000:
                print("enter between 0 and 10000 ")
                continue
            toBinary(user)
            break
        except ValueError:
            print("check the input")
