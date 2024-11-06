#Write a program that prompts the user to enter a number within the range of 1 through 10.
#The program should display the Roman numeral version of that number. If the number is
#outside the range of 1 through 10, the program should display an error message. The following
#table shows the Roman numerals for the numbers 1 through 10:
#           Number  Roman Numeral
#             1          I
#             2          II
#             3         III
#             4          IV
#             5           V
#             6          VI
#             7          VII
#             8         VIII
#             9          IX
#             10          X

#User input
number = int(input("Enter a number between 1 through 10: "))

message = ""

#Conditions
if number < 1 or number > 10:
    message = "Error. Please enter a number between 1 through 10"
else:
    message = "Number " + format(number) + " Roman Numeral is "
    
    if number == 1:
        message += "I"
    elif number == 2:
        message += "II"
    elif number == 3:
        message += "III"
    elif number == 4:
        message += "IV"
    elif number == 5:
        message += "V"
    elif number == 6:
        message += "VI"
    elif number == 7:
        message += "VII"
    elif number == 8:
        message += "VIII"
    elif number == 9:
        message += "IX"
    elif number == 10:
        message += "X"
        
print(message)