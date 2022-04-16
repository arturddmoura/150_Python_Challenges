#Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.

total = float(input('What was the total price of the bill? '))
diners = int(input('How many people ate? '))

division = float(total) / diners

print(f'Each person must pay {division}.')

