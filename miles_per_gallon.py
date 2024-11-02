#A car's miles-per-gallon (MPG) can be calculated with the following formula:
#       MPG = Miles driven ÷ Gallons of gas used
#Write a program that asks the user for the number of miles driven and the gallons of gas
#used. It should calculate the car's MPG and display the result. 

#Prompt the user
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallos that will be used for the trip: "))

#Calculate the miles per gallon
MPG = miles_driven / gallons_used

#print("The MPG for this trip is ", MPG)
print("The MPG for this trip is ", format(MPG, '.2f'))