#Make a maths quiz that asks five questions by randomly generating two whole numbers to make the question (e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At the end of the quiz, tell them how many they got correct out of five.
import random
question = 0
score = 0

for question in range (0,5):
    num1 = random.randint(0,1000)
    num2 = random.randint(0,1000)
    res = num1 + num2
    
    user = int(input(f'How much is {num1} + {num2}? '))
    if res == user:
        score = score + 1
    
    else:
        score = score + 0

print(f'You got {score} correct answers out of 5! ')