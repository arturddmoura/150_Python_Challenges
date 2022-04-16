#Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”.

n1 = int(input("Please type a number between 10 and 20: "))
    
if n1 >= 10 and n1 <= 20:
        print("Thank you.")

else:
    print("Incorrect answer.")