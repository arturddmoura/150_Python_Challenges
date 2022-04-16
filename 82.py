#Show the user a line of text from your favourite poem and ask for a starting and ending point. Display the characters between those two points.
poem = "Because I could not stop for Death, he kindly stopped for me. "
print(poem)

start = int(input("Please enter a starting point: "))
end = int(input("Please enter an ending point. "))

print(poem[start:end])