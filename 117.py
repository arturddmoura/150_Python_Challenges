#Create a simple maths quiz that will ask the user for their name and then generate two random questions. Store their name, the questions they were asked, their answers and their final score in a .csv file. Whenever the program is run it should add to the .csv file and not overwrite anything.
import random
import csv

name = input("What is your name? ")

r1 = random.randint(0,10)
r2 = random.randint(0,10)
r3 = random.randint(0,10)
r4 = random.randint(0,10)

question1 = str(r1) + " + " + str(r2) + " = "
question2 = str(r3) + " + " + str(r4) + " = "
score = 0
res1 = int(input(question1))
if res1 == (r1 + r2):
    score = score + 1

res2 = int(input(question2))
if res2 == (r3 + r4):
    score = score + 1

file = open("Scores.csv", "a")
student = name + ", " + str(question1) + ", " + str(res1) + ", " + str(question2) + ", " + str(res2) + ", " + str(score) + " points\n"
file.write(student)

file.close()

