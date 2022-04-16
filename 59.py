#Display five colours and ask the user to pick one. If they pick the same as the program has chosen, say “Well done”, otherwise display a witty answer which involves the correct colour, e.g. “I bet you are GREEN with envy” or “You are probably feeling BLUE right now”. Ask them to guess again; if they have still not got it right, keep giving them the same clue and ask the user to enter a colour until they guess it correctly.
import random

color = random.choice(['Red', 'Green', 'Blue', 'Yellow', 'Purple'])
print(color)
user = input('Please pick a color: ')

if user.upper() == color.upper():
    print('Well done!')

elif color.upper() != user.upper():

    while color == 'Green' and user.upper() != color.upper():
        print("I bet you're GREEN with envy. ")
        user = input('Please pick a color: ')

    while color == 'Red' and user.upper() != color.upper():
        print("I bet you're RED with anger. ")
        user = input('Please pick a color: ')

    while color == 'Blue' and user.upper() != color.upper():
        print("I bet you're BLUE right now. ")
        user = input('Please pick a color: ')

    while color == 'Purple' and user.upper() != color.upper():
        print("I bet you're PURPLE right now. ")
        user = input('Please pick a color: ')

    while color == 'Yellow' and user.upper() != color.upper():
        print("I bet you're pissing yourself YELLOW. ")

print('Correct! ')