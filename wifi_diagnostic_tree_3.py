#Figure 3-19 shows a simplified flowchart for troubleshooting a bad Wi-Fi connection. Use
#the flowchart to create a program that leads a person through the steps of fixing a bad
#Wi-Fi connection. Here is an example of the program’s output:
#
#Reboot the computer and try to connect.
#Did that fix the problem? no Enter
#Reboot the router and try to connect.
#Did that fix the problem? yes Enter
#
#Notice the program ends as soon as a solution is found to the problem. Here is another
#example of the program’s output:
#Reboot the computer and try to connect.
#Did that fix the problem? no Enter
#Reboot the router and try to connect.
#Did that fix the problem? no Enter
#Make sure the cables between the router and modem are plugged in firmly.
#Did that fix the problem? no Enter
#Move the router to a new location.
#Did that fix the problem? no Enter
#Get a new router.

print('Please follow the following troubleshooting steps \n' +
      'if you experience a bad Wi-Fi connection.')
print('Reboot the computer and try to connect again. \n')
steps = input('Did that fix the problem? ')

if steps == 'no' or steps == 'NO' or steps == 'n' or steps == 'N':
    print('Reboot the router and try to connect.')
    steps = input('Did that fix the problem? ')
        
    if steps == 'no' or steps == 'NO' or steps == 'n' or steps == 'N':
        print('Make sure the cables between the router and modem are plugged in firmly.')
        steps = input('Did the fix the problem? ')
        
        if steps == 'no' or steps == 'NO' or steps == 'n' or steps == 'N': 
            print('Move the router to a new location.')
            steps = input('Did the fix the problem? ')
            
            if steps == 'no' or steps == 'NO' or steps == 'n' or steps == 'N':
                print('Get a new router.')
            else:
                print('The problem has been resolved no further actions.')
        else:
            print('The problem has been resolved no further actions.')
    else:
        print('The problem has been resolved no further actions.')
else:
    print('The problem has been resolved no further actions.')
    

