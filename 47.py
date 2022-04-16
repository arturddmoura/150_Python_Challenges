#Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. Once the loop has stopped, display the total.

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))

res = number1 + number2

question = input("Do you want to add another number? ")

while question.upper() == "Y":
    number3 = int(input("Please enter another number: "))
    res = res + number3
    question = input("Do you want to enter another number? ")

print(f"The total is {res}")
