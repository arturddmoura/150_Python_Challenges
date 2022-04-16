#Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess correctly, display the message “Well done”, otherwise tell them if they are too high or too low and ask them to pick a second number. If they guess correctly on their second guess, display “Correct”, otherwise display “You lose
import random

number = random.randint(1, 5)
user = int(input('Please pick a number: '))

if number == user:
    print('Well done! ')

elif number < user:
    print('Too high! ')
    user = int(input('Please pick a number: '))
    if number == user:
        print('You win! ')

    else:
        print('You lose!')
        print({number})


elif number > user:
    print('Too low! ')
    user = int(input('Please pick a number: '))
    if number == user:
        print('You win! ')

    else:
        print('You lose!')