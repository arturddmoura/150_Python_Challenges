#Ask the user to enter an integer that is over 500. Work out the square root of that number and display it to two decimal places.
import math

number = int(input("Please enter a number over 500: "))

while number < 500:
    number = int(input("Please try again: "))

number = math.sqrt(number)
print(round(number, 2))