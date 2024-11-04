#Write a program that asks the user for the number of males and the number of females registered in class.
#The program should display the percentage of males and females in the class.
#Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the class.
#The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage of females can be calculated
#as 12 ÷ 20 = 0.6, or 60%.

males = float(input('Enter the number of males registered in class: '))
females = float(input('Enter the number of females registered in class: '))

#Calculations
#total_males = (males + females) / males
#total_females = (females + males) / females
total_students = males + females
males_percentange = males / total_students
females_percentage = females / total_students

print("The percentage of males students are: ", format(males_percentange, ',.2f'))
print("The percentage of females students are: ", format(females_percentage, ',.2f'))
