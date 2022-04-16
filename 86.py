#Ask the user to enter a new password. Ask them to enter it again. If the two passwords match, display “Thank you”. If the letters are correct but in the wrong case, display the message “They must be in the same case”, otherwise display the message “Incorrect”.
password = input("Please enter a new password: ")
confirmation = input("Please enter your password again: ")

if password == confirmation:
    print("Thank you! ")

elif password.upper() == confirmation.upper():
    print("They must be in the same case! ")

else:
    print("Incorrect! ")