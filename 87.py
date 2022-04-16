#Ask the user to type in a word and then display it backwards on separate lines. For instance, if they type in “Hello” it should display as shown below:
user = input("Please type a word: ")
lenght = len(user)

for i in range (lenght - 1, -1, -1):
    print(user[i])
