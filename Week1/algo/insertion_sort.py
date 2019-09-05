"""
 ******************************************************************************
 *  Purpose: to InsertionSort
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""

from Week1.Utility.utility import InsertionSort

# insertion sort is used for the below program where we have used unsorted list
if __name__ == '__main__':

    # list is created and passed to the function
    llist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    InsertionSort(llist)
    print(llist)    # here sorted list is printed using insertion sort

