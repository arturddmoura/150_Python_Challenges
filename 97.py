#Using the 2D list from program 096, ask the user to select a row and a column and display that value.

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Please select a row: "))
column = int(input("Please select a column: "))

print(list[row][column])
