# 2.28 What are three advantages of using named constants?
# ANSWER:
#   1. they make programs more self-explanatory.
#   2. widespread changes can easily be made to the program
#   3. they help to prevent the typographical errors that are
#      common when using magic numbers.

# 2.29 Write a Python statement that defines a named constant 
# for a 10 percent discount.
DISCOUNT_PERCENT = .0255
print('Discount percent = ', format(DISCOUNT_PERCENT, '.2%'))