#Ask the user to type in their name and then tell them how many vowels are in their name.
count = 0

name = input("Please type your name: ")

for letters in name:
    if letters.lower() == "a" or letters.lower() == "e" or letters.lower() == "i" or letters.lower() == "o" or letters.lower() == "u":
        count = count + 1

print(f"There are {count} vowels in your name. ")