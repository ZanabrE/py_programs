#One pound is equivalent to 0.454 kilograms. Write a program that asks the user to enter
#the mass of an object in pounds and then calculates and displays the mass of the object 
#in kilograms.

mass = int(input("Enter the mass of the object in pounds: "))

convertion = mass * 0.454

print("The mass of the object in killograms is ", format(convertion, '.2f'), "Kg")