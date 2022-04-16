#Create the following pattern:
import turtle
import random

for i in range (0,10):

    turtle.pendown()
    turtle.color(random.choice(["red", "green", "blue", "purple", "pink", "orange"]))
    turtle.begin_fill()

    for i in range (0,8):
        turtle.forward(50)
        turtle.left(45)

    turtle.penup()
    turtle.end_fill()
    turtle.right(35)

turtle.exitonclick()