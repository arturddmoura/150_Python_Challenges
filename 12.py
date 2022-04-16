#Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second.

n1 = int(input("Please type the first number: "))
n2 = int(input("Please type the second number: "))

if n1 > n2:
    print(n2)
    print(n1)

else:
    print(n1)
    print(n2)