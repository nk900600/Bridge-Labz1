# import json
#
# with open("state_city_json") as f:
#     data = json.load(f)
#
# print(data[0].keys())
import re
while True:
    try:

        fullname=input("enter : ")
        regex = re.compile("\w+.\w+", re.IGNORECASE)

        if re.search("\w+.\w+", fullname) is True:
            print(" enter vaild full name ")
            continue
        break
    except ValueError:
        print("val")











# while True:
#     flag = 0
#     try:
#         user = input("enter city:")
#
#         for j in data[0]["maharastra"].values():
#             if j == user:
#                 print("fg")
#                 flag = 1
#                 break
#         if flag == 1:
#             break
#         for j in data[0]["gujrat"].values():
#             if j == user:
#                 print("done")
#                 flag=1
#                 break
#         if flag == 1:
#             break
#         for j in data[0]["punjab"].values():
#             if j == user:
#                 print("done")
#                 flag=1
#                 break
#         if flag == 1:
#             break
#     except ValueError:
#         print("dj")
