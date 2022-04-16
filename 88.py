#Ask the user for a list of five integers. Store them in an array. Sort the list and display it in reverse order.
from array import *

numbers = array('i', [])

for i in range(0,5):
    user = int(input("Please enter one number: "))
    numbers.append(user)

numbers = sorted(numbers)
numbers.reverse()

print(numbers)