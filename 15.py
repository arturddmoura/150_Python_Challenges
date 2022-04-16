#Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”.

red = input("What is your favourite colour? ")

if red.upper() == "RED":
    print("I like red too!")

else:
    print(f"I don't like {red}, i prefer red.")
