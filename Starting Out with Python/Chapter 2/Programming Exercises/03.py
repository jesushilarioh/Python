#
# 3. Pounds to Kilograms
# 
# One pound is equivalent to 0.454 kilograms. Write a 
# program that asks the user to enter the mass of an 
# object in pounds and then calculates and displays 
# the mass of the object in kilograms.
# 

ONE_POUND_IN_KILOGRAMS = .454
object_mass_pounds = float(input('\nEnter mass of an object: '))
object_mass_kilograms = object_mass_pounds * ONE_POUND_IN_KILOGRAMS
print('Object in kilograms =', format(object_mass_kilograms, ',.2f'), end='\n\n')