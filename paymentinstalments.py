#Write a program that asks the user to enter the amount of a purchase and the desired
#number of payment instalments. The program should add 5 percent to the amount to get
#the total purchase amount, and then divide it by the desired number of instalments, then
#display messages telling the user the total amount of the purchase and how much each
#instalment will cost. 
#Variable
percentage = .05

amount = float(input("Enter the amount of a purchase: "))
payments = int(input("Enter the desired number of payment instalments: "))

#Calculate the five percent to the amount
percentage_amount = (amount * percentage) + amount

#Calculate the desired number of instalments
instalments = percentage_amount / payments

print("The total amount of purchase is $", format(percentage_amount, '.2f'))
print("The total amount of each instalment cost is $", format(instalments, '.2f'))