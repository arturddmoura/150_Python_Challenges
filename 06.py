#Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a user- friendly format.

slices = int(input('How many slices have you started with? '))
eaten = int(input('Hoa many slices have you eaten? '))

result = slices - eaten
print(f'You have {result} slices left.')