#A software company sells a package that retails for $99. Quantity discounts are given
#according to the following table:
#           Quantity    Discount
#             10–19        10%
#             20–49        20%
#             50–99        30%
#             100 or more  40%
#Write a program that asks the user to enter the number of packages purchased. The program
#should then display the amount of the discount (if any) and the total amount of the
#purchase after the discount.

#Variable
package_price = 99

#user input
number_of_package = float(input('Enter the number of package you wish to buy: '))

#Conditions
if number_of_package < 0:
    print('Error. Please enter a number of packages greater than 0.')
else:
    discount = 0
    
    if number_of_package < 10:
        discount = 0
        
    elif number_of_package >= 10 and number_of_package <= 19:
        discount = .10
        
    elif number_of_package >= 20 and number_of_package <= 49:
        discount = .20
    
    elif number_of_package >= 50 and number_of_package <= 99:
        discount = .30
        
    elif number_of_package >= 100:
        discount = .40
    
#Calculations
total_price = number_of_package * package_price
total_discount = (total_price) * discount
total_amount = total_price - total_discount

print('You have bought ', number_of_package, ' packages and you will get a ', format(discount,'.0%'), 'discount')
print('Your total is ', total_price)
print('Your total amount is ', total_amount)
    
