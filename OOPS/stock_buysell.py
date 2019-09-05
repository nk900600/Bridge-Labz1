"""
 ******************************************************************************
 *  Purpose:  stock buy or sell
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week2.node_linked_and_sorted import LinkedList, Node
import json
from OOPS.oops_util import Stock
from Week2.util import Stack, Queue1
import datetime


# company shares are added to the
def Company_Shares():
    global add, remove
    st = Stock("stock_json")  # object is created for stock and linked list
    llist = LinkedList()
    stack = Stack()
    q = Queue1()

    with open("stock_json") as f:  # json file is loaded
        data = json.load(f)

    while True:
        flag = 0

        try:  # try is used for the finding exception

            userinput = int(input("number of stocks you want to add or removed : "))
            if userinput >= 5 or userinput <= 0:
                print("user input should be between 0-5")
                continue

            for i in range(userinput):
                # input is taken from the user
                for stocks in range(len(st.Only_Stocks())):
                    print("**", st.Only_Stocks()[i], end=" ")  # will display all the stocks in the portfolio
                user = int(input("\nenter 1 to add or enter 2 to delete or enter 3 to exit :"))
                if user >= 4 or user <= 0:
                    print("enter between 0-4")
                    flag = 1
                    continue

                if flag == 1:
                    break

                if user == 1:
                    added = st.Buy()[1]
                    stack.Push(added)
                    print()
                    llist.Add(stack.Size()[0]["stock"])  # if user is given 1 we will ad the stock to the linked list
                    now = datetime.datetime.now()
                    q.AddRear(now)

                elif user == 2:
                    remove = st.Sell()
                    stack.Push(data[remove])
                    llist.Add(stack.Size()[0]["stock"])
                    now1 = datetime.datetime.now()
                    q.AddRear(now1)

                else:
                    print("bye bye")  # program will end here

            llist.Print()  # final linked list is printed with the symbol which were added o removed
            print()
            q.PrintList()  # final linked list is printed from queue function where time stamp of the add or remove is
            # updated

            st.Dump("stock_json")  # this method is used for appending the data in JSON format
            break

        except (ValueError, TypeError):
            print(" please check the  Error ")


# main function is created
if __name__ == '__main__':
    Company_Shares()
