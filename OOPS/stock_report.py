"""
 ******************************************************************************
 *  Purpose:  stock Report
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
from OOPS.oops_util import Stock


# function is created
def Stock_Report():

    stock = Stock("stock_json")     # object is created for the class
    print("number of stocks in the portfolio are ", stock.Print()[2])
    print("total number of share to hold from all the stocks", stock.Print()[1])
    print("approx amount paid of per stock in your portfolio is ", stock.Print()[0])


# main function is created and updated
if __name__ == '__main__':
    Stock_Report()
