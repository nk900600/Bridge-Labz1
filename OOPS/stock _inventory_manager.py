"""
 ******************************************************************************
 *  Purpose:  stock update
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from OOPS.oops_util import Stock
import json


# stock update is created to buy or sell stock
def Stock_Update():
    # object class is created
    stock = Stock("stock_json")
    while True:
        try:

            num = int(input("how many stock you wish to add in in your portfolio :"))  # input is taken for updating the
            if num >= 5:
                print("can only add 4 stocks in one run")
                continue
            break
        except ValueError:
            print("check input")

    # portfolio
    if num == 0:  # if input is 0 then this function will return
        print(" no stocks to be added in the portfolio ")
        pass
    for i in range(num):  # for loop is used for adding or removing the data
        stock.Buy()
        print("stock is added to the portfolio")
        while True:
            flag = 0
            try:  # try is used to catch the exception
                for stocks in range(len(stock.Only_Stocks())):
                    print(stock.Only_Stocks()[stocks], end="--")

                print(" choose from above stocks to delete ")
                user = int(input("\npress 1 for portfolio report \npress 2 for removing \npress 3  to exit  "))
                if user >= 4:
                    print("choose from above option")
                    continue

                if user == 1:  # if input is 1 then over all report will be printed
                    print("number of stocks in the portfolio are ", stock.Print()[2])
                    print("total number of share to hold from all the stocks", stock.Print()[1])
                    print("approx amount paid of per stock in your portfolio is ", stock.Print()[0])
                    flag = 1

                if user == 2:  # if input is 2 then stock will be deleted
                    stock.Sell()
                    print("stock have been deleted")
                    print(stock.Only_Stocks())

                if user == 3:  # if input is 3 then program will end
                    print("thank you for using the service")

                break
            except ValueError:  # exception is used for the same
                print("please check the input ")
        break
    stock.Dump("stock_json")  # this method is used for appending the data in JSON format


# main function is created and called
if __name__ == '__main__':
    Stock_Update()
