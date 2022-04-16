#Create an array of five numbers between 10 and 100 which each have two decimal places. Ask the user to enter a whole number between 2 and 5. If they enter something outside of that range, display a suitable error message and ask them to try again until they enter a valid amount. Divide each of the numbers in the array by the number the user entered and display the answers shown to two decimal places.
from array import *
import math

list1 = array ('f', [20.25, 30.25, 40.25, 50.25, 60.25])

user = int(input("Please enter a whole number between 2 and 5: "))

while user > 5 or user < 2:
    user = int(input("Try again! Please enter a whole number between 2 and 5: "))

for i in range (0,5):
    result = list1[i] / user
    print(round(result, 2))