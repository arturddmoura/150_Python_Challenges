#Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as The answer is [answer].

n1 = int(input('Please enter the first number: '))
n2 = int(input('Please enter the second number: '))
n3 = int(input('Please enter the third number: '))

result = (n1 + n2) * n3
print(f'The answer is {result}.')