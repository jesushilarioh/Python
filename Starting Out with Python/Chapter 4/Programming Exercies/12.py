#
# 12. Calculating the Factorial of Number 
#
# In mathematics, the notation n! represents the factorial of the nonnegative integer n. The
# factorial of n is the product of all the nonnegative integers from 1 to n. For example,
#
#   7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5,040  
#
# and
#
#   4! = 1 x 2 x 3 x 4 = 24 
#
# Write a program that lets the user enter a nonnegative integer then uses a loop to calculate
# the factorial of that number. Display the factorial.
#
#

user_number = int(input("Enter a positive number: "))

while user_number < 0:
    user_number = int(input("Error. Enter a positive number: "))

total = 0

if user_number > 0:
    total = 1
    
    for number in range(user_number):
        total *= (number + 1)

output = format(total)

print(output)