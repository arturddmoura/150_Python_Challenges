#Ask the user to enter five numbers. Sort them into order and present them to the user. Ask them to select one of the numbers. Remove it from the original array and save it in a new array.
from array import *

list1 = array ('i', [])
list2 = array ('i', [])

for i in range (0,5):
    user = int(input("Please enter a number: "))
    list1.append(user)

print(sorted(list1))

getRid = int(input("Please select the number you want to remove: "))

list1.remove(getRid)
list2.append(getRid)

print(sorted(list1))
print(sorted(list2))