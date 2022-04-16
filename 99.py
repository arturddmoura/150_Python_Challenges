# Change your previous program to ask the user which row they want displayed. 
# Display that row. Ask which column in that row they want displayed and display the value that is held there.
# Ask the user if they want to change the value. If they do, ask for a new value and change the data. 
# Finally, display the whole row again.

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Which row would you like displayed? "))
print(list[row])

column = int(input("Which column in the row do you want displayed? "))
print(list[row][column])

question = input("Do you want to change the value? ")

if question.upper() == "YES":
    new_value = int(input("What is the new value? "))
    list[row][column] = new_value

print(list[row])