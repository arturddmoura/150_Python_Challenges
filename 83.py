#Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again. Keep repeating this until they type in a message all in uppercase.
user = input("Please type in a word in upper case: ")

while user != user.upper():
    user = input("Plese try again: ")

print(f"Thank you! You typed: {user}! ")