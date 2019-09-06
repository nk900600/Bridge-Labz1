
"""
 ******************************************************************************
 *  Purpose:  playing card function
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from numpy import sort

from OOPS.oops_util import CardGame
from Week2.util import Queue1


# playing card function is created
def Playing_Card():

    Que = Queue1()
    cards = CardGame()  # object is created for card game
    data = cards.Distribute()  # distribute function is called from card game and results will be printed in 2d array
    # print(data)   # distributed card will be printed out
    for hand in data:  # for loop is used for adding each players cards to the linked list
        Que.AddRear(hand)
    # hands are updated to the queue via linked list
    print()
    Que.PrintList()     # same distributed cards are printed out in linked list format in queue


# main function is created and called
if __name__ == '__main__':
    Playing_Card()
