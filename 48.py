#Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the party and then display how many people they have coming to the party.
count = 0

name = input("Who do you want to invite to the party? ")
print(f"{name} has now been invited. ")
count = count +1

question = input("Do you want to invite anyone else? ")

while question.upper() == "Y":
    name = input("Who do you want to invite to the party? ")
    print(f"{name} has now been invited. ")
    count = count + 1
    question = input("Do you want to invite anyone else? ")

print(f"{count} people have been invited to the party.")