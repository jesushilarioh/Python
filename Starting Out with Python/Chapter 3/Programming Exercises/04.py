# 4. Roman Numerals
# Write a program that prompts the user to enter 
# a number within the range of 1 through 10. 
# The program should display the Roman numeral 
# version of that number. If the number is outside 
# the range of 1 through 10, the program should 
# display an error message. The following table 
# shows the Roman numerals for the numbers 
# 1 through 10:
#
# Number      Roman Numeral
# 1           I 
# 2           II 
# 3           III 
# 4           IV 
# 5           V 
# 6           VI 
# 7           VII 
# 8           VIII 
# 9           IX
# 10          X

user_number = int(input('Enter a number betwee 1 and 10: '))

if user_number == 1:
    print('The roman numeral for', user_number, 'is I')
elif user_number == 2:
    print('The roman numeral for', user_number, 'is II')
elif user_number == 3:
    print('The roman numeral for', user_number, 'is III')
elif user_number == 4:
    print('The roman numeral for', user_number, 'is IV')
elif user_number == 5:
    print('The roman numeral for', user_number, 'is V')
elif user_number == 6:
    print('The roman numeral for', user_number, 'is VI')
elif user_number == 7:
    print('The roman numeral for', user_number, 'is VII')
elif user_number == 8:
    print('The roman numeral for', user_number, 'is VIII')
elif user_number == 9:
    print('The roman numeral for', user_number, 'is IX')
elif user_number == 10:
    print('The roman numeral for', user_number, 'is X')
else:
    print('Error. Number must be between 1 and 10.\n' + 
          'Rerun program and try again.')