# 
# 11. Male and Female Percentages
# 
# Write a program that asks the user for the 
# number of males and the number of females 
# registered in a class. The program should 
# display the percentage of males and females 
# in the class.
# 
# Hint: Suppose there are 8 males and 12 females 
# in a class. There are 20 students in the class. 
# The percentage of males can be calculated as 
# 8 ÷ 20 = 0.4, or 40%. The percentage of females can 
# be calculated as 12 ÷ 20 = 0.6, or 60%.
# 

number_of_males = int(input('Enter the number of males: '))
number_of_females = int(input('Enter the number of females: '))

total_number_of_students = number_of_females + number_of_males

percentage_of_males = number_of_males / total_number_of_students
print('Total number of males =', format(percentage_of_males, '.0%'))

percentage_of_females = number_of_females / total_number_of_students
print('Total number of females =', format(percentage_of_females, '.0%'))