import random

def randomAdd():
    r1 = random.randint(5,20)
    r2 = random.randint(5,20)
    answer = r1 + r2

    user_answer = int(input(f"{r1} + {r2} = "))
    return answer, user_answer

def randomSub():
    r1 = random.randint(25,50)
    r2 = random.randint(1,25)
    answer = r1 - r2

    user_answer = int(input(f"{r1} - {r2} = "))
    return answer, user_answer

def checkAnswer(answer, user_answer):
    if answer == user_answer:
        print(f"Correct! The answer was {user_answer}! ")
    
    else:
        print(f"Incorrect! The answer was {answer}! ")

def main():
    user_choice = int(input("1) Addition.\n2) Subtraction.\nPlease select 1 or 2: "))
    if user_choice == 1:
        answer, user_answer = randomAdd()
        checkAnswer(answer, user_answer)

    elif user_choice == 2:
        answer, user_answer = randomSub()
        checkAnswer(answer, user_answer)

    else:
        print("Invalid option! ")
        
main()