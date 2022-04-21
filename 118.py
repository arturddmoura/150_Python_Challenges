#Define a subprogram that will ask the user to enter a number and save it as the variable “num”. 
# Define another subprogram that will use “num” and count from 1 to that number.

def enterNumber():
    num = int(input("Please enter a number: "))
    return num

def countFromNum(num) :
    for i in range (1, num + 1):
        print (i)
    
def main():
    num = enterNumber()
    countFromNum(num)

main()