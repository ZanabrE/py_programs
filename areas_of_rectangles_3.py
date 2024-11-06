#The area of a rectangle is the rectangle's length times its width. Write a program that asks
#for the length and width of two rectangles. The program should tell the user which rectangle
#has the greater area, or if the area are the same. 

#User input
lengthA = float(input("Enter the length of a rectangle A: "))
widthA = float(input("Enter the width of a rectangle A: "))
lengthB = float(input("Enter the length of a rectangle B: "))
widthB = float(input("Enter the width of a rectangle B: "))

#Calculations
area1 = lengthA * widthA
area2 = lengthB * widthB

#Conditons
if area1 > area2:
    print("Rectangle A has the greater area at", area1, "inches")
elif area2 > area1:
    print("Rectangle B has the greater area at", area2, "inches")
elif area1 == area2:
    print("Rectangel A and rectangle B has the same area at ", area1, "inches")
    