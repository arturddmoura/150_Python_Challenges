#Display an array of five numbers. Ask the user to select one of the numbers. Once they have selected a number, display the position of that item in the array. If they enter something that is not in the array, ask them to try again until they select a relevant item.
from array import *

list = array ('i', [1, 2, 3, 4, 5])
tryagain = True

print(list)
user = int(input("Please select a number from the list: "))

while tryagain == True:
    if user in list:
        print(f"Number {user} is number {list.index(user)} on the list. ")
        tryagain = False

    else:
        print("Try again!")
        user = int(input("Please select a number from the list: "))
