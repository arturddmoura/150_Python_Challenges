#Ask the user to enter the names of three people they want to invite to a party and store them in a list. After they have entered all three names, ask them if they want to add another. If they do, allow them to add more names until they answer “no”. When they answer “no”, display how many people they have invited to the party.

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