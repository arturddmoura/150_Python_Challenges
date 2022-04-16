#Create a list of four three-digit numbers. Display the list to the user, showing each item from the list on a separate line. Ask the user to enter a three-digit number. If the number they have typed in matches one in the list, display the position of that number in the list, otherwise display the message “That is not in the list”.

list = [100, 200, 300, 400]

for i in list:
    print(i)

user = int(input("Please enter a three digit number: "))

if user in list:
    print(f"The number you entered is number {list.index(user)} on the list. ")

else:
    print("That is not on the list. ")