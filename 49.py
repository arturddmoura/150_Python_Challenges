#Create a variable called compnum and set the value to 50. Ask the user to enter a number. While their guess is not the same as the compnum value, tell them if their guess is too low or too high and ask them to have another guess. If they enter the same value as compnum, display the message “Well done, you took [count] attempts”.

compnum = 50
count = 0

user = int(input("Please enter a number: "))

while user != compnum:
    
    if user > compnum:
        print("Too high! ")
        count = count + 1
        user = int(input("Please enter a number: "))

    
    elif user < compnum:
        print("Too low! ")
        count = count + 1
        user = int(input("Please enter a number: "))

print(f"Good job, it took you {count} tries. ")
    
