import random 

# Define a subprogram that will ask the user to pick a low and a high number, 
# and then generate a random number between those two values and store it in a variable called “comp_num”.
def pickLowHigh():
    high = int(input("Please pick a high number: "))
    low = int(input("Please pick a low number: "))
    comp_num = random.randint(low, high)
    print(comp_num)
    return comp_num

# Define another subprogram that will give the instruction “I am thinking of a number...”
#  and then ask the user to guess the number they are thinking of.
def thinkingNumber():
    print("I was thinking of a number...")
    user_guess = int(input("What is the number I'm thinking of? "))
    return user_guess

# Define a third subprogram that will check to see if the comp_num is the same as the user’s guess. 
# If it is, it should display the message “Correct, you win”, otherwise it should keep looping, 
# telling the user if they are too low or too high and asking them to guess again until they guess correctly.

def checkAnswer():
    comp_num = pickLowHigh()
    user_guess = thinkingNumber()

    while user_guess != comp_num:
        if user_guess > comp_num:
            user_guess = int(input("Too high! Try again: "))

        elif user_guess < comp_num:
            user_guess = int(input("Too low! Try again: "))
            
    print("You win!")

checkAnswer()