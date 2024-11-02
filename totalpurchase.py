#A customer in a store is purchasing five items. Write a program that asks for the price 
#of each item, then displays the subtotal of sale, the amount of sales tax, and the total.
#Assume that sales tax is 7 percent.

#User prompt
price1 = float(input("The price for this item is "))
price2 = float(input("The price for this item is "))
price3 = float(input("The price for this item is "))
price4 = float(input("The price for this item is "))
price5 = float(input("The price for this item is "))

#Calculation for the cost of the item
subtotal_of_sale = price1 + price2 + price3 + price4 + price5

#Calculate the sales tax
sales_tax = subtotal_of_sale * 0.07

#Total of sales
total = subtotal_of_sale + sales_tax

#Total of the sales
print("The item cost $", price1)
print("The sales tax is $", format(sales_tax, '.2f'))
print("The total is $", total)

