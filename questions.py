# This code will prompt some questions
print("*********************************")
print("         Multiple Choice         ")
print("*********************************")
print()
print("1. A(n)________ is a set of instructions that a computer follows to perform a task.")
print("a.compiler")
print("b.program")
print("c.interpreter")
print("d.programming language")
#Variables
a = 'compiler'
b = 'program'
c = 'intrepreter'
d = 'programming language'

answer = input("Enter your answer: ")
#Conditioning the user input.
if answer == b:
    print("Correct!")
else:
    print("Incorrect!")
    
print()
print("2. The physical devices that a computer is made of are referred to as _____________.")
print("a.hardware")
print("b.software")
print("c.the operating system")
print("d.tools")
#Variables
a = 'hardware'
b = 'software'
c = 'the operating system'
d = 'tools'

answer2 = input("Enter your answer: ")
if answer2 == a:
    print("Correct!")
else:
    print("Incorrect!")
