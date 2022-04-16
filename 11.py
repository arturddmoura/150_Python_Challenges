#Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.
count = 0

over100 = int(input('Enter a number over 100: '))
under10 = int(input('Enter a number under 10: '))

result = over100 // under10
print(f'The smaller number goes into the larger number {result} time(s). ')

#while over100 > 0:
#    over100 = over100 - under10
#    count = count + 1

#print(f'The smaller number goes into the larger number {count} time(s). ')
