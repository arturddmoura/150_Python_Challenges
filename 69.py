#Create a tuple containing the names of five countries and display the whole tuple. Ask the user to enter one of the countries that have been shown to them and then display the index number (i.e. position in the list) of that item in the tuple.

countries_tuple = ("Argentina", "Brazil", "Chile", "Bolivia", "Uruguai")
print(countries_tuple)

user = input("Please enter the name of one of the countries shown: ")
print(f"{user} is number {countries_tuple.index(user)} on the list. ")