#Add to program 069 to ask the user to enter a number and display the country in that position.
countries_tuple = ("Argentina", "Brazil", "Chile", "Bolivia", "Uruguai")
print(countries_tuple)

user = int(input("Please enter the number of one of the countries shown: "))
print(f"The country in position {user} is {countries_tuple[user]} ")