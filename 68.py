#Draw a pattern that will change each time the program is run. Use the random function to pick the number of lines, the length of each line and the angle of each turn.
import random
import turtle

for i in range (0,random.randint(5,20)):
        turtle.forward(random.randint(25,100))
        turtle.right(random.randint(1,360))

turtle.exitonclick()