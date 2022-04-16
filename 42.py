#Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want that number included. If they do, then add the number to the total. If they do not want it included, don’t add it to the total. After they have entered all five numbers, display the total.

total = 0
res = 0

while total < 5:
    numbers = int(input("Please input a number: "))
    question = input("Do you want it added to the total? ")

    if question.upper() == "YES":
        res = res + numbers
        total = total + 1
    
    else:
        total = total + 1

print(f"The total is {res}.")