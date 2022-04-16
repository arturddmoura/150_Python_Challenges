#Ask the user to enter the radius of a circle (measurement from the centre point to the edge). 
#Work out the area of the circle (π*radius2).

import math

radius = int(input("Please enter the radius of a circle: "))

result = math.pi * (radius ** 2)
print(result)
