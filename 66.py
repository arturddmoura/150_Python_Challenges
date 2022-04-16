#Draw an octagon that uses a different colour (randomly selected from a list of six possible colours) for each line.
import turtle
import random

for i in range (0,8):
    turtle.color(random.choice(["red", "green", "blue", "purple", "pink", "orange"]))
    turtle.forward(100)
    turtle.left(45)

turtle.exitonclick()
