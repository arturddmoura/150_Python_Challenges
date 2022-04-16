#Create a list containing the titles of four TV programmes and display them on separate lines. Ask the user to enter another show and a position they want it inserted into the list. Display the list again, showing all five TV programmes in their new positions.

shows = ["Naruto", "Bleach", "Soul Eater", "Demon Slayer"]

for i in shows:
    print(i)

user_input = input("Please enter another show: ")
position = int(input(f"In which position do you wish to add {user_input}? "))

shows.insert(position, user_input)
print(shows)