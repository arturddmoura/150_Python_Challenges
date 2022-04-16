#Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”, otherwise display “Thank you”.

n1 = int(input("Please type a number under 20: "))

if n1 >= 20:
    print("Too high.")

elif n1 < 20:
    print("Thank you.")