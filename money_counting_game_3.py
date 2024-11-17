#Create a change-counting game that gets the user to enter the number of coins required
#to make exactly one dollar. The program should prompt the user to enter the number of
#pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one
#dollar, the program should congratulate the user for winning the game. Otherwise, the
#program should display a message indicating whether the amount entered was more than
#or less than one dollar.

#Variables
QUARTERS = .25
DIME = .10
NICKEL = .05
PENNIE = .01

message = ''

#User input
quarters = float(input('How many quarters will be entered: '))
dime = float(input('How many dimes will be enetered: '))
nickel = float(input('How many nickels will be enetered: '))
pennie = float(input('How many pennies will be entered: '))

#Calculations
quarters *= QUARTERS
dime *= DIME
nickel *= NICKEL
pennie *= PENNIE

total_coins =  quarters + dime + nickel + pennie

if total_coins == 1.00:
    message = 'It is a dollar.'
else:
    message = 'It is NOT a dollar.\n'
    
    if total_coins > 1.00:
        message += 'It is greater than a dollar. Please enter the information again!'
    else:
        message += 'It is less than a dollar. Please enter the information again!'


print(message)