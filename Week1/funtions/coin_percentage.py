"""
 ******************************************************************************
 *  Purpose: coin toss
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import CoinToss


# program is called from the main function
if __name__ == '__main__':
    while True:
        try:
            toss = int(input("number of flips: "))
            if toss <= 1 or toss >= 100:
                print("please enter the number between 0 and 100 ")
                continue
            CoinToss(toss)
            break
        except ValueError:
            print(" check the input")