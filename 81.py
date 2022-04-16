#Ask the user to type in their favourite school subject. Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.
user = input("What is your favourite school subject? ")

for letter in user:
    print(letter,end="-")