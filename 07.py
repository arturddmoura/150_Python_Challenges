#Ask the user for their name and their age. Add 1 to their age and display the output [Name] next birthday you will be [new age].

name = input('What is your name? ')
age = int(input('How old are you? '))

age = age + 1

print(f'{name}, on your next birthday you will be {age}.')