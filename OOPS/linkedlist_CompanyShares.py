"""
 ******************************************************************************
 *  Purpose:  company shares buy or sell
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from Week2.node_linked_and_sorted import LinkedList, Node
import json
from OOPS.oops_util import Stock


# compan shares function is created
def Company_Shares():
    global user
    st = Stock("stock_json")  # object is created for stock and linked list
    llist = LinkedList()
    with open("stock_json") as f:  # json file is loaded
        data = json.load(f)
    for items in data:  # json file is converted in linked list
        llist.Add(items)
    # input is taken from the user
    while True:
        try:  # try is used for the finding exception

            for i in range(len(st.Only_Stocks())):  # will display all the stocks in the portfolio
                print("**", st.Only_Stocks()[i], end=" ")
            print("\nchoose from above stocks to delete stocks ")
            user = int(input("enter 1 to add or enter 2 to delete or enter 3 to exit :"))

            if user >= 4 or user <= 0:
                print("check input")
                continue
            if user == 1:
                llist.Add(st.Buy()[1])  # if user is given 1 we will ad the stock to the linked list
                llist.Print()
            elif user == 2:
                g = st.Sell()  # if user is given 2 we will call stock class to delete the data
                llist.Remove(data[g])  # here data is removed
            else:
                print("bye bye")  # program will end here
            st.Dump("stock_json")
            break
        except ValueError:
            print(" please check the Value Error ")


# main function is created and called
if __name__ == '__main__':
    Company_Shares()
