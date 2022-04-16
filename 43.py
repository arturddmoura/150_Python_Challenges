#Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number and then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down from 20 to that number. If they entered something other than up or down, display the message “I don’t understand”.

question = input("Which direction do you want to count, up or down? ")

if question.upper() == "UP":
    number = int(input("Please select a top number: "))
    
    for i in range (1, number + 1):
        print(i)

elif question.upper() == "DOWN":
    number = int(input("Enter a number below 20: "))

    for i in range (20, number - 1, - 1):
        print(i)

else:
    print("I don't understand.")