"""
 ******************************************************************************
 *  Purpose:  rice wheat and pulses inventory
 *
 *  @author  Nikhil Kumar
 *  @version 3.7
 *  @since   24/08/2019
 ******************************************************************************
"""
import json


# json function is created
def json_inventory():
    with open("JSON", "r") as f:  # json file is loaded in dict format
        data = json.load(f)

    riceinvent = 0
    wheatinvent = 0
    pulseinvent = 0

    try:  # try exception is used id data is not present in the inventory

        # to file data in each inventory
        for i in data["Rice"]:
            for price in i:
                riceinvent += i["price per kg"]  # data is incremented

        for i in data["wheat"]:
            for price in i:
                wheatinvent += i["price per kg"]  # data is incremented

        for i in data["pulses"]:
            for price in i:
                pulseinvent += i["price per kg"]  # data is incremented

    except TypeError:
        print(" there is type error ")

    print("""total value for rice in inventory is {},\ntotal value for wheat in inventory is {},
total value for pulse in inventory is {}""".format(riceinvent, wheatinvent, pulseinvent))

    dump = json.dumps("JSON")
    # print(type(dump))  # then data is dumped in str format


# main function is created and called
if __name__ == '__main__':
    json_inventory()
