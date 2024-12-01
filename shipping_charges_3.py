#The Fast Freight Shipping Company charges the following rates:
#       Weight of Package                            Rate per Pound
#       2 pounds or less                                  $1.50
#       Over 2 pounds but not more than 6 pounds          $3.00
#       Over 6 pounds but not more than 10 pounds         $4.00
#       Over 10 pounds                                    $4.75
#Write a program that asks the user to enter the weight of a package then displays the shipping
#charges.

weight_of_package = float(input('Enter the weight of a package: '))

if weight_of_package <= 2:
    rate_per_pound = 1.50
elif weight_of_package >= 2 and weight_of_package <= 6:
    rate_per_pound = 3.00
elif weight_of_package >= 6 and weight_of_package <= 10:
    rate_per_pound = 4.00
elif weight_of_package > 10:
    rate_per_pound = 4.75
    
#Calculations
shipping_charges = weight_of_package * rate_per_pound

print('Shipping charges are: ', format(shipping_charges, ',.2f'))
