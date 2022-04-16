#Ask the user to enter two numbers. Use whole number division to divide the first number by the second and also work out the remainder and display the answer in a user-friendly way (e.g. if they enter 7 and 2 display “7 divided by 2 is 3 with 1 remaining”)

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

result = n1 // n2
remainder = n1 % n2

print(f"{n1} divided by {n2} is {result} with {remainder} remaining.")