# This program will calculate the percentage 
# and the the future investment of any individual (page-77).
# This program will also calculate the average 
# of every amount invested (page-81).
# This program will tell you how much an individual will get 
# in annual return in their savings account.

# 1.Get the original price of the item.
original_price = float(input("Enter amount you want to invest: "))

# 2.Get the years of investment.
years_invesment = float(input("Enter the year of investment: "))

# 2.Calculate 20 percent of the original price. This is the amount of the dicount.
years_invesment = original_price * 0.6

# 3.Substract the discount from the original price. This is the sale price.
#sale_price = original_price - discount

# 4.Display the sale price. 
print('Annually investment return $', years_invesment)

# Invesment average 
print('------------------------------------------------------------')
print('This section will give an average of three different invesment accounts')

# Get the first amount.
amount1 = float(input('Enter the first amount of invesment: '))

# Get the second amount.
amount2 = float(input('Enter the second amount of invesment: '))

# Get te third amount.
amount3 = float(input('Enter the third amount of invesment: '))

# Calculate the average.
average_invesment = (amount1 + amount2 + amount3) / 3.0

# Display the average invesment.
print('The average invesment for the three acounts are $', format(average_invesment, ',.2f'))

# Annual sabvings.
print('------------------------------------------------------------')
print('This section will give an annual savings information')

# 1.Get the desire future value.
future_value = float(input('Enter the desired future value: '))

# 2.Get the annual interest rate.
rate = float(input('Enter the annual interest rate: '))

# 3.Get the number of years that the money will sit in the account.
years = int(input('Enter the number of years the money will grow: '))

# 4.Calculate the amount that will have to be deposited.
present_value = future_value / (1.0 + rate)**years

# 5.Display the result of the calculation in step 4.
print('You will need to deposit this amount: $', format(present_value, ',.2f'), sep='')