#A class has two tests worth 25 points each along with a main exam worth 50 points. For a student
#to pass the class, they must obtain an overall score of at least 50 points, and must obtain at
#least 25 points in the main exam. If a student’s total score is less than 50 or they obtain less than
#25 points in the main exam, they receive a grade of “Fail”. Otherwise, their grade is as follows:
#           If they get more than 80, they get a grade of “Distinction”. 50–59 = “Pass”.
#           If they get less than 80 but more than 60, they get a “Credit” grade.
#           If they get less than 60, they get a ”Pass” grade.
#Write a program that prompts the user to enter their points for both tests and the exam and
#converts the values to integers. The program should first check if the points entered for the
#tests and exam are valid. If any of the test scores are not between 0 and 25, or the exam
#score is not between 0 and 50, the program should display an error message. Otherwise,
#the program should display the total points and the grade.

message = ''
#User input
test1 = int(input("Enter points for test 1: "))
#Conditions
if test1 >= 0 and test1 <= 25:
    test2 = int(input("Enter points for test 2: "))
    
    if test2 >= 0 and test2 <= 25:
        exam = int(input("Enter points for the exam: "))
        
        if exam >= 0 and exam <= 50:
            #Calculations
            final_total = test1 + test2 + exam
            
            if final_total < 50 or exam < 25:
                message = 'Fail.'
                
            else:
                if final_total > 80:
                    message = 'Distinction'
                elif final_total > 60 or final_total < 80:
                    message = 'Credit'
                elif final_total < 60:
                    message = 'Pass'
        else:
            message = 'Invalid. Points for the exam is bettwen 0 - 50.'
    else:
        message = 'Invalid. Points for test two is between 0 - 25.'
else:
    message = 'Invalid. Points for test one is between 0 - 25.'

print(message)   
#print('Test 1 you have ', test1, 'points')
#print('Test 2 you have ', test2, 'points')
#print('Exam you have ', exam, 'points')
#print('Your grade is '+ str(final_total) + '')