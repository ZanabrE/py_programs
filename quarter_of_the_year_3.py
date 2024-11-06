#Write a program that asks the user for a month as a number between 1 and 12. The
#program should display a message indicating whether the month is in the first quarter,
#the second quarter, the third quarter, or the fourth quarter of the year. Following are the
#guidelines:
#• If the user enters either 1, 2, or 3, the month is in the first quarter.
#• If the user enters a number between 4 and 6, the month is in the second quarter.
#• If the number is either 7, 8, or 9, the month is in the third quarter.
#• If the month is between 10 and 12, the month is in the fourth quarter.
#• If the number is not between 1 and 12, the program should display an error.

#User input
month = int(input("Enter the month as a number: "))

message = ""

#Conditions
if month < 1 or month > 12:
    message = "Error. The number must be between 1 and 12.\n" + \
              "Please run the program again."
else:
    message = "Month " + format(month) + " is in the"
    
    if month >= 1 or month <= 3:
        message += " first"
    elif month >= 4 or month <= 6:
        message += " second"
    elif month >= 7 or month <= 9:
        message+= " third"
    elif month >= 10 or month <= 12:
        message += " fourth"
    
    message += " quarter."

print(message)
