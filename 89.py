#Create an array which will store a list of integers. Generate five random numbers and store them in the array. Display the array (showing each item on a separate line).
from array import *
import random

list = array ('i', [])

for i in range (0,5):
    number = random.randint(0,5000)
    list.append(number)

for i in list:
    print(i)