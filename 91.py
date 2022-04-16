#Create an array which contains five numbers (two of which should be repeated). Display the whole array to the user. Ask the user to enter one of the numbers from the array and then display a message saying how many times that number appears in the list.
from array import *

list = array ('i', [1, 2, 2, 3, 4])

print(list)

user = int(input("Please enter one of the numbers from the array: "))
print(f"Number {user} appears {list.count(user)} time(s) in the list.")