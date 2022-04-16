#Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is between 10 and 20, display “Correct”, otherwise display “Too high”.

n1 = int(input("Please type a number: "))

if n1 < 10:
    print("Too low.")

elif n1 >= 10 and n1 <= 20:
    print("Correct.")

else: 
    print("Too high.")