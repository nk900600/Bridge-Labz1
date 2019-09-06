"""
 ******************************************************************************
 *  Purpose:  oops util stock,card game, address book
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
import json
import numpy as np
import random
import itertools


# stock class is made here
class Stock:

    def __init__(self, filename):  # here file is initialised with file name
        with open(filename) as f:
            self.data = json.load(f)  # data is loaded in this function
            # print(self.data)

    def Buy(self):  # here stock is added to the database
        while True:
            try:  # try is used to catch user input error
                stock = input("name the stock you want to add : ")
                if stock.isalpha() is not True or len(stock) >= 10:
                    print("enter vaild stock")
                    continue
                total_share = int(input("number of share you want to buy : "))
                if total_share >= 1001 or total_share <= 0:
                    print("min shares=1 ,max shares=1000")
                    continue
                share_price = np.random.randint(100, 200)
                break
            except ValueError:  # here below statement will be printed out
                print("check the input data")
        dict1 = {"stock": stock, "total_share": total_share, "share_price": share_price}
        z = self.data  # data is added in dict file which is appended to data
        z.append(dict1)
        return z, dict1  # now function is return

    def Print(self):  # this function is used for printing the data
        shareprice = 0
        totalshare = 0
        share = 0
        for stocks in range(len(self.data)):  # for loop is used for traversing the dict
            share += 1
            shareprice = shareprice + self.data[stocks]["share_price"]
            totalshare = totalshare + self.data[stocks]["total_share"]
        return shareprice, totalshare, share  # we have returned the total shares,share price and total share

    def Sell(self):  # this function is used for deleting the stock
        global user
        while True:
            flag = 0
            try:
                user = input("stock name to delete from the portfolio :")
                for i in range(len(self.Only_Stocks())):
                    if self.Only_Stocks()[i] == user:
                        flag = 1
                        break
                if flag == 1:
                    break
            except ValueError:
                print("value error")

        g = -1
        for i in self.data:
            g += 1
            # print(i['stock'])
            if i['stock'] == user:
                del self.data[g]  # data is deleted from the json file
                return g  # here we have a return value of the index

    def Dump(self, filename):  # file is saved and write back to the original file
        with open('stock_json', 'w') as f:
            json.dump(self.data, f, indent=2)

    def Only_Stocks(self):  # this function is used for displaying only stocks
        stocks = []
        for i in range(len(self.data)):
            stocks.append(self.data[i]["stock"])
        return stocks  # stocks val is returned an displayed in the main file


# card game class is created
class CardGame:

    def __init__(self):  # here we have created rank and suites variables

        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "ace", "jack", "queen", "king"]
        self.suits = ["heart", "diamonds", "spade", "clubs"]
        self.deck = list(itertools.product(self.suits, self.rank))

        #
        #     rank=(self.rank,self
        # for i in self.rank:
        #     self.deck.append(str(i))
        # for i in self.suits:
        #     self.deck.append(i)

    def Distribute(self):  # this function is used for distributing cards in even format
        deck = self.deck
        while True:  # loop is used for taking input if wrong entered
            try:
                players = int(input("number of player playing: "))  # number of players want to play
                if players >= 6 or players <= 0:
                    print("number of player can be 1 to 5")
                    continue
                break
            except ValueError:
                print("check the input")
        array = [[] for i in range(players)]  # 2d array is created to store the value
        for i in range(players):  # using random function deck is shuffled
            random.shuffle(deck)
            for j in range(9):  # this loop is used for distributing data to the players
                array[i].append(deck[j])
        return array  # final cards stored in array var


# address book class is made
class AddressBook:  # address book class is created

    def __init__(self, filename):  # here file is initialised with file name
        with open(filename) as f:
            self.file = json.load(f)  # json file is loaded

    def Add(self):  # this function is used for added data to the json file
        while True:
            try:
                first_name = input("enter your first name :")
                if first_name.isalpha() is False:
                    print("enter vaild name ")
                    continue

                last_name = input("enter your last name :")
                if last_name.isalpha() is False:
                    print("enter vaild last name")
                    continue

                address = input("enter your 1st and 2nd line of address :")
                if len(address) >= 60:
                    print("length of address should be less than 60")
                    continue
                cities = self.cities()
                for i in cities:
                    print("**", i, end=" ")

                while True:
                    flag = 0
                    try:
                        city = input("\nenter the city name from above list :")
                        for i in cities:
                            if city == i:
                                flag = 1
                                break
                        if flag == 1:
                            break
                    except ValueError:
                        print("error")

                with open("state_city_json") as f:
                    country = json.load(f)

                while True:
                    flag = 0
                    state = None
                    for state in range(len(country)):
                        for i in country[state]["maharastra"].values():
                            if city == i:
                                state = "maharastra"
                                flag = 1
                                break
                    if flag == 1:
                        break
                    for state in range(len(country)):
                        for i in country[state]["gujrat"].values():
                            if city == i:
                                flag = 1
                                state = "gujrat"
                                break
                    if flag == 1:
                        break
                    for state in range(len(country)):
                        for i in country[state]["punjab"].values():
                            if city == i:
                                state = "punjab"
                                flag = 1
                                break
                    if flag == 1:
                        break

                print("As per city your state is ", state)
                zipcode = int(input("enter the zip code :"))
                if len(str(zipcode)) >= 7:
                    print("length of input should be less than 7")
                    continue

                phone_number = int(input("enter the full mobile number"))
                if phone_number <= 916000000000 or phone_number >= 920000000000:
                    print("enter vaild number starting from 91")
                    continue
                break
            except ValueError:
                print("please check user input and start from the top")

        # dic is used for storing user input data
        dic = {"first_name": first_name,
               "last_name": last_name,
               "address": address,
               "city": city,
               "state": state,
               "zipcode": zipcode,
               "phone_number": phone_number}
        print("user data added successfully")

        add = self.file
        add.append(dic)  # user data is added to the file

        print(dic)  # now data and input data is called in main file

    def Delete(self):  # this function is used for deleting data in the json file
        # input is used for deleting data
        while True:

            flag = 0
            try:
                datadelete = input("\nname of the person you want to delete from the address book:")
                for i in range(len(self.Only_Names())):
                    if self.Only_Names()[i] == datadelete:
                        flag = 1
                        break
                if flag == 1:
                    break
            except ValueError:
                print("value error")
        name = []
        for i in range(len(self.file)):
            name.append(self.file[i]["first_name"])
        index = -1  # index is used for keeping track of the index where we have to delete the data
        print()
        print(datadelete, "is deleted from address book ")
        for para in self.file:  # para is used for transversing through the data
            index += 1
            if datadelete == para["first_name"]:  # if condition is used for checking user input
                del self.file[index]  # here data is deleted if data  matches
                return index  # index is returned for future
        print(datadelete, " is deleted from address book ")

    def Print(self):  # this function is used for printing data in mailing format
        data = self.file
        for i in range(len(data)):  # for loop is used transversing values through data
            for j in data[i].values():
                print(j)
            print()

    def Sort(self):  # sort function is used for sorting the data in json file
        array = []
        data = self.file  # data is stored in var
        for i in range(len(self.file)):  # first name is appended in array
            array.append((self.file[i]["first_name"]))
        name_sort = sorted(array)  # here only names are sorted
        sorteddata = []  # this empty array is used for storing sorted file
        for i in name_sort:  # nested loop is used for matching sorted names to file
            for j in range(len(data)):
                if i == data[j]["first_name"]:
                    sorteddata.append(data[j])  # if name matches then data is appended

        self.file = sorteddata  # now we have swapped data with sorted data
        return sorteddata  # here we have return sorted data

    def Dump(self, filename):  # thsi function is used for dumping edited data to the json file
        with open('address_book_json', 'w') as f:
            json.dump(self.file, f, indent=2)

    def Only_Names(self):  # this function is used for printing only names from the file
        data = self.file
        name = []
        for i in range(len(data)):
            # print("**", (data[i]["first_name"]), end=" ")
            name.append(data[i]["first_name"])
        return name

    def cities(self):
        with open("state_city_json") as f:
            country = json.load(f)
        cities = []
        for i in range(len(country)):
            for j in country[i]["maharastra"].values():
                cities.append(j)
        for i in range(len(country)):
            for j in country[i]["gujrat"].values():
                cities.append(j)
        for i in range(len(country)):
            for j in country[i]["punjab"].values():
                cities.append(j)
        return cities
