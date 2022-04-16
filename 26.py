#Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case.

word = input("Please type a word: ")
number = len(word)
first = word[0]

if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
    print((word + "way").lower())

else:
    print((word [1:number] + word[0] + "ay").lower())