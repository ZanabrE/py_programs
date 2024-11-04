#Last month, Joe purchased some stock in Acme Software,Inc. Here are the details of the purchase:
#The number of shares that Joe purchased was 2,000
#When Joe purchased the stock, he paid $40.00 per share. 
#Joe paid his stockbrocker a commission that amounted to 3 percent of the amount paid for the stock. 
#
#Two weeks later, Joe sold the stock. Here are the details of the sale:
#The number of shares that Joe sold was 2,000
#He sold the stock for $42.75 per share. 
#He paid his stockbroker another commission that ammounted to 3 percent of the amount he received for th stock. 
#
#Write a program that displays the following information:
#The amount of money Joe paid for the stock
#The amount of commission Joe paid his broker when he bought the stock. 
#The amount for which Joe sold the stock. 
#The amount of commission Joe paid his broker when he sold the stock.
#Display the amount of money that Joe had left when he sold the stock and paid his
#broker (both times). If this amount is positive, then Joe made a profit. If the amount is 
#negative, then Joe lost money. 

#Variables
shares_purchased = 2000
shares_cost = 40
shares_sold = 42.75
commission_percentage = 0.03

#Calculations
stock_paid = shares_purchased * shares_cost
commission_paid_purchased = stock_paid * commission_percentage
stock_sold = shares_purchased * shares_sold
commission_paid_sold = stock_sold * commission_percentage
profit_loss = stock_sold - (commission_paid_purchased + commission_paid_sold)

#Displaying the information
print("The amount of money Joe paid for the stock is $", format(stock_paid, ',.2f'), end='\n')
print("The amount of commission Joe paid his broker when he bought the stock is $", format(commission_paid_purchased, ',.2f'), end='\n')
print("The amount for which Joe sold the stock is $", format(stock_sold, ',.2f'), end='\n')
print("The amount of commission Joe paid his broker when he sold the stock is $", format(commission_paid_sold, ',.2f'), end='\n')
print("The amount of profit/loss Joe has after paying his broker is $", format(profit_loss, ',.2f'), end='\n')

