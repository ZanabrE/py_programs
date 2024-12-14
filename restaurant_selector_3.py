#You have a group of friends coming to visit for your high school reunion, and you want
#to take them out to eat at a local restaurant. You aren’t sure if any of them have dietary
#restrictions, but your restaurant choices are as follows:
#
#Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
#Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
#Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
#Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
#The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
#
#Write a program that asks whether any members of your party are vegetarian, vegan, or
#gluten-free, to which then displays only the restaurants to which you may take the group.
#Here is an example of the program’s output:
#Is anyone in your party a vegetarian? yes Enter
#Is anyone in your party a vegan? no Enter
#Is anyone in your party gluten-free? yes Enter
#
#Here are your restaurant choices:
#   Main Street Pizza Company
#   Corner Cafe
#   The Chef's Kitchen
#
#Here is another example of the program’s output:
#
#Is anyone in your party a vegetarian? yes Enter
#Is anyone in your party a vegan? yes Enter
#Is anyone in your party gluten-free? yes Enter
#
#Here are your restaurant choices:
#   Corner Cafe
#   The Chef's Kitchen

vegetarian = input('Is anyone in your party a vegetarian? ')

if vegetarian == 'yes' or vegetarian == 'no':
    vegan = input('Is anyone in your party a vegan? ')
    
    if vegan == 'yes' or vegan == 'no':
        gluten_free = ('Is anyone in your party gluten-free? ')
        
        if gluten_free == 'yes' or gluten_free == 'no':
            print('Here are the list of the restaurants.')
else: 
    print('Please enter a restaurant option.')
    