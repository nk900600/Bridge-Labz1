"""
 ******************************************************************************
 *  Purpose: to Merge_Sort
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week1.Utility.utility import Merge_Sort

# below merge sort is used for sorting list
if __name__ == '__main__':
    llist = [5, 9, 1, 2, 4, 8, 6, 3, 7]
    print(llist)  # here unsorted list is printed
    Merge_Sort(llist)  # her list is sorted using merge sort
    print(llist)  # now sorted list is printed
