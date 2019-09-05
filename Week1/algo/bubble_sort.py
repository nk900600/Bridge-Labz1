"""
 ******************************************************************************
 *  Purpose: bubble sort
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""

from Week1.Utility.utility import BubbleSort

# we have imported bubble sort from the utility


if __name__ == '__main__':

    # below  list is used for the bubble sort

    number = [1, 2, 5, 4, 54]

    BubbleSort(number)    # here we have used bubble sort for unsorted list
    print(number)     # here we have printed out the sorted list

