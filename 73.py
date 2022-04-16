#Ask the user to enter four of their favourite foods and store them in a dictionary so that they are indexed with numbers starting from 1. Display the dictionary in full, showing the index number and the item. Ask them which they want to get rid of and remove it from the list. Sort the remaining data and display the dictionary.
food_dict = {}
index = 1

for i in range (0,4):
    foodinput = input("Please enter one of your favourite foods: ")
    food_dict[index] = foodinput
    index = index + 1
print (food_dict)

user = int(input("Enter the number of the item you want to remove: "))
del food_dict[user]
print(sorted(food_dict.values()))
