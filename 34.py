#Display the following message:
#If the user enters 1, then it should ask them for the length of one of its sides and display the area.
#If they select 2, it should ask for the base and height of the triangle and display the area. 
# If they type in anything else, it should give them a suitable error message.

menu = int(input("1) Square.\n2) Triangle.\n\nEnter a number: "))

if menu == 1:
    lenght = int(input("What is the lenght of one side of the square?"))
    area_square = lenght * lenght
    print(f"The area of the square is {area_square}")

elif menu == 2:
    base = int(input("What is the base of the triangle?"))
    height = int(input("What is the height of the triangle?"))
    area_triangle =  (base * height) / 2 
    print(f"The area of the triangle is {area_triangle}.")

else:
    print("Please enter a valid option.")