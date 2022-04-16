#Ask for the radius and the depth of a cylinder and work out the total volume (circle area*depth) rounded to three decimal places.
import math

radius = int(input("Please insert the radius of the circle: "))
depth = int(input("Please insert the depth of the cylinder: "))

area = math.pi * (radius ** 2)
volume = area * depth
print(round(volume, 3))

