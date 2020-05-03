# 
# 10. Ingredient Adjuster
# 
# A cookie recipe calls for the following ingredients:
# 
# • 1.5 cups of sugar
# • 1 cup of butter
# • 2.75 cups of flour
# 
# The recipe produces 48 cookies with this amount of 
# the ingredients. Write a program that asks the user 
# how many cookies he or she wants to make, then 
# displays the number of cups of each ingredient 
# needed for the specified number of cookies.
# 

# asks the user how many cookies he or she wants to make,
number_of_cookies = int(input('\nHow many cookies would you like to make: '))

# displays the number of cups of each ingredient 
# needed for the specified number of cookies.
COOKIES = 48
SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75

total_sugar  = (SUGAR * number_of_cookies) / COOKIES
total_butter = (BUTTER * number_of_cookies) / COOKIES
total_flour  = (FLOUR * number_of_cookies) / COOKIES

print('\nNumber of cookies =', number_of_cookies, end='\n\n')
print('Total sugar =', format(total_sugar, ',.2f'))
print('Total butter =', format(total_butter, ',.2f'))
print('Total flour =', format(total_flour, ',.2f'), end='\n\n')