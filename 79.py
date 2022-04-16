#Create an empty list called “nums”. Ask the user to enter numbers. After each number is entered, add it to the end of the nums list and display the list. Once they have entered three numbers, ask them if they still want the last number they entered saved. If they say “no”, remove the last item from the list. Display the list of numbers.
num_list = []

for i in range (0,3):
    user = int(input("Please enter a number: "))
    num_list.append(user)
    print(num_list)
    
question = input("Do you still want the last number entered to be saved? ")

if question.upper() == "NO":
    num_list.remove(user)

print(f"The final list is: {num_list}" )