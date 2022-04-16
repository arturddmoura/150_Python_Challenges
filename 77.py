#Change program 076 so that once the user has completed their list of names, display the full list and ask them to type in one of the names on the list. Display the position of that name in the list. Ask the user if they still want that person to come to the party. If they answer “no”, delete that entry from the list and display the list again.

list = []
more = "NO"

for i in range (0,3):
    person = input("Enter the name of the person you want to invite to the party: ")
    list.append(person)

more = input("Do you want to invite another person? ")

while more.upper() == "YES":
    person = input("Enter the name of the person you want to invite to the party: ")
    list.append(person)
    more = input("Do you want to invite another person? ")

else:
    print(f"You invited {len(list)} people to the party. ")

print(list)
user = input("Type one of the names in the list: ")
print(f"{user} is number {list.index(user)} on the list." )

user2 = input(f"Do you still want {user} to come to the party? ")
if user2.upper() == "NO":
    list.remove(user)
    print(list)

else:
    print(list)
