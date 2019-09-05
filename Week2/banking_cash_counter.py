"""
 ******************************************************************************
 *  Purpose: banking cash simulator
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week2.util import Queue
from Week1.Utility.utility import Total


# cash balance functions is created and function is called
def Cash_Balance(length):
    while True:
        try:  # try exception is used for the error if any
            q = Queue()  # object is created from Queue class
            fd = Total(length)

            for items in length:  # items are enqueued  and updated on the queue
                q.Enqueue(items)
                items += 1

            user_input = int(input("enter the amount  : "))  # user input for amount
            if user_input <= 0 or user_input >= 1000:
                print("enter the number between 0 and 1000")
                continue

            for data in range(len(length)):  # now for loop is used for checking the data
                if length[data] == user_input:  # if length is equal, data will be de-queued and enqueued to maintain
                    # cash
                    q.Dequeue()
                    return

            if Total(length) != fd:  # enqueued function is used to add
                q.Enqueue(100)

            Total(length)
            print(q.Size())
            break

        except ValueError:  # if value error occurred try function will catch
            print("please check the input ")


# main function is called
if __name__ == '__main__':
    # list function is called

    llist = [100, 100, 100]
    Cash_Balance(llist)
