#The date June 10, 1960, is special because when it is written in the following format, the
#month times the day equals the year:
#6/10/60
#Design a program that asks the user to enter a month (in numeric form), a day, and a two digit
#year. The program should then determine whether the month times the day equals the
#year. If so, it should display a message saying the date is magic. Otherwise, it should display
#a message saying the date is not magic.

#User input
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
year = int(input("Enter the year: "))

message = format(month) + '/' + format(day) + '/' + format(year) + ' IS '

if ((month * day) != year):
    message += 'NOT'
message += ' magic'

print(message)
    
#if month == 6 or day == 10 or year == 60:
#    print(month, '/',  day, '/', year, " that date is magic")
#else:
#    print(month, '/', day, '/', year, " that date is not magic")
    