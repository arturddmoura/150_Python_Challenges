#Ask the user to type in their postcode. Display the first two letters in uppercase.
user = input("Please enter your postcode: ")

user = user[0:2]
print(user.upper())