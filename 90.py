#Ask the user to enter numbers. If they enter a number between 10 and 20, save it in the array, otherwise display the message “Outside the range”. Once five numbers have been successfully added, display the message “Thank you” and display the array with each item shown on a separate line.
from array import *

list = array ('i', [])

while len(list) < 5:
    user = int(input("Enter a number: "))

    if user <= 20 and user >= 10:
        list.append(user)
    
    else:
        print("Outside of range! ")

print("Thank you!")

for i in list:
    print(i)