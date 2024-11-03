#A cookie recipe calls for the following ingridients:
#1.5 cups of sugar
#1 cup of butter
#2.75 cups of flour
#The recipe produces 48 cookies with this amount of the ingridients. Write a program that 
#asks the user how many cookies he or she wants to make, then displays the number of cups
#of each ingridient needed for the specified number of cookies.

#Variables
cookies = 48
sugar = 1.5
butter = 1
flour = 2.75

cookies_made = float(input("How many cookies do you want to make? "))

#Calculations
sugar_cups = (sugar * cookies_made) / cookies
butter_cup = (butter * cookies_made) / cookies
flour_cups = (flour * cookies_made) / cookies

print("Number of cookies: ", cookies_made)
print("Sugar needed is ", format(sugar_cups, ',.2f'), "cups")
print("Butter needed is ", format(butter_cup, ',.2f'), "cup")
print("Flour needed is ", format(flour_cups, ',.2f'), "cups")