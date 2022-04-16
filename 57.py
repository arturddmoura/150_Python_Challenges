#Update program 056 so that it tells the user if they are too high or too low before they pick again.
import random

number = random.randint(1,10)
user = int(input('Please pick a number: '))

while user != number:
    if user > number:
        print('Too high! ')
        user = int(input('Please pick a number: '))
    
    elif user < number:
        print('Too low! ')
        user = int(input('Please pick a number: '))