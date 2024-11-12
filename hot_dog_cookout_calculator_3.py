#Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a
#program that calculates the number of packages of hot dogs and the number of packages of
#hot dog buns needed for a cookout, with the minimum amount of leftovers. The program
#should ask the user for the number of people attending the cookout and the number of hot
#dogs each person will be given. The program should display the following details:
#• The minimum number of packages of hot dogs required
#• The minimum number of packages of hot dog buns required
#• The number of hot dogs that will be left over
#• The number of hot dog buns that will be left over

#Variables
HOT_DOGS = 10
HOT_DOGS_BUNS = 8

number_of_people = int(input("How many people will be attending to the cookout: "))
hot_dogs_per_person = int(input("How many hot dogs each person will be given: "))

#Calculations
total_hot_dogs = number_of_people * hot_dogs_per_person
number_hot_dogs_required = total_hot_dogs / HOT_DOGS
number_hot_dogs_buns_required = total_hot_dogs / HOT_DOGS_BUNS
number_hot_dogs_left_over = total_hot_dogs % HOT_DOGS
number_hot_dogs_buns_left_over = total_hot_dogs % HOT_DOGS_BUNS

print('The minimum number of packages of hot dogs required ', number_hot_dogs_required)
print('The minimum number of packages of hot dog buns required ', number_hot_dogs_buns_required)
print('The number of hot dogs will be left over are ', number_hot_dogs_left_over)
print('The number of hot dog buns that will be left over are ', number_hot_dogs_buns_left_over)
