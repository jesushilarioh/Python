# 3.14 What is a compound Boolean expression?
# ANSWER: 
# when logical operators allow you to connect 
# multiple Boolean expressions.

# 3.15 The following truth table shows various combinations 
# of the values true and false connected by a logical operator. 
# Complete the table by circling T or F to indicate whether the 
# result of such a combination is true or false.
# Logical Expression
#---------------------
# True and False    = F
# True and True     = T
# False and True    = F
# False and False   = F
# True or False     = T
# True or True      = T
# False or True     = T
# False or False    = F
# not True          = F
# not False         = T

# 3.16 Assume the variables a = 2, b = 4, and c = 6. 
# following conditions to indicate whether its value is 
# true or false.
#--------------------
# a == 4 or b > 2       = T
# 6 <= c and a > 3      = F
# 1 != b and c != 3     = T
# a >= −1 or a <= b     = T
# not (a > 2)           = T

# 3.17 Explain how short-circuit evaluation works with the 
# and and or operators.
# ANSWER:
# With the and operator, if the expression on the left is false, 
# the expression on the right will not be checked.

# With the or operator, if the expression on the left is true,
# the expression on the right will not be checked.

# 3.18 Write an if statement that displays the message “The 
# number is valid” if the value referenced by speed is within 
# the range 0 through 200.
speed = 80
if speed >= 0 and speed <= 200:
    print('The number is valid')

# 3.19 Write an if statement that displays the message “The 
# number is not valid” if the value referenced by speed is 
# outside the range 0 through 200.
speed = 300
if speed < 0 or speed > 200:
    print('The number is not valid')