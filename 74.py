#Enter a list of ten colours. Ask the user for a starting number between 0 and 4 and an end number between 5 and 9. Display the list for those colours between the start and end numbers the user input.
colours = ["Red", "Green", "Blue", "Purple", "Brown", "White", "Black", "Orange", "Yellow", "Pink"]

start = int(input("Please select a starting number between 0 and 4: "))
end = int(input("Please select an ending number between 5 and 9: ")
)
print(colours[start:end])