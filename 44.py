#Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and after each name display “[name] has been invited”. If they enter a number which is 10 or higher, display the message “Too many people”.

number = int(input("How many friends do you want to invite to the party? "))

if number <= 10:
    for i in range (1, number + 1):
        name = input(f"What is the name of the guest #{i}? ")
        print(f"{name} has been invited.")

elif number > 10:
    print("Too many people.")