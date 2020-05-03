# 
# 9. Circle Measurements
# Write a program that asks the user to enter 
# the radius of a circle. The program should 
# calculate and display the area and 
# circumference of the circle using πr2 for 
# the area and 2πr for the circumference.
# 
# Hint:You can either use 3.14159 as the value
# of pi(π),or add the statement "import math" 
# to the start of the program and then use 
# "math.pi" wherever you need the value of 
# pi in the program.
# 
import math

# asks the user to enter the radius of a circle.
radius = float(input('\nEnter the radius of a circle: '))

# calculate and display the area and 
# circumference of the circle using πr2 for 
# the area and 2πr for the circumference.
area = math.pi * (radius**2)
circumference = 2 * math.pi * radius

print('Radius =', radius)
print('Area =', area)
print('Circumference = ', circumference, end='\n\n')