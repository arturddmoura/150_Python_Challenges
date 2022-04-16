#Randomly pick a whole number between 1 and 10. Ask the user to enter a number and keep entering numbers until they enter the number that was randomly picked
import random

number = random.randint(1,10)
user = int(input('Please pick a number: '))

while user != number:
    user = int(input('Please pick a number: '))