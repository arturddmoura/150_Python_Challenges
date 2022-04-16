#Create two arrays (one containing three numbers that the user enters and one containing a set of five random numbers). Join these two arrays together into one large array. Sort this large array and display it so that each number appears on a separate line.
from array import *
import random

list1 = array ('i', [])
list2 = array ('i', [])

for i in range (0,3):
    user = int(input("Please enter a number: "))
    list1.append(user)

for i in range (0, 5):
    user2 = random.randint(1,1000)
    list2.append(user2)

final_list = list1 + list2
final_list = sorted(final_list)

for i in final_list:
    print(i)