#Write a program that calculates the total amount of a meal purchased at a restaurant.
#The program should ask the user to enter the charge for the food, then calculate the amounts
#of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

#Variables
PERCENT_TIP = 0.18
SALES_TAX = 0.07

#Prompt the user
meal = float(input("Enter the total amount of the meal purchased: "))

#Calculate the tip
amount_tip = meal * PERCENT_TIP

#Calculate the sales tax
total_sales_tax = amount_tip * SALES_TAX

#Calculate the total
total = meal + amount_tip + total_sales_tax

print("The meal cost $", format(meal, '.2f'), sep='')
print("The tip is $", format(amount_tip, '.2f'), sep='')
print("The sales tax is $", format(total_sales_tax, '.2f'), sep='')
print("The total for the purchase of the meal is $", format(total, '.2f'), sep='')