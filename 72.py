#Create a list of six school subjects. Ask the user which of these subjects they don’t like. Delete the subject they have chosen from the list before you display the list again.

subjects = ["Math", "History", "Geography", "Literature", "Biology", "English"]
print(subjects)

user = input("What is the subject you dislike the most? ")
subjects.remove(user)
print(subjects)