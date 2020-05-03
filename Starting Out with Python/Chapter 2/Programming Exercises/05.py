# 
# 5. Distance Traveled
# 
# Assuming there are no accidents or delays, the 
# distance that a car travels down the 
# interstate can be calculated with the 
# following formula:
# 
#   Distance = Speed * Time
# 
# A car is traveling at 70 miles per hour. Write a program that displays the following:
# • The distance the car will travel in 6 hours
# • The distance the car will travel in 10 hours
# • The distance the car will travel in 15 hours
# 
SPEED = 70

time = 6
distance = SPEED * time
print('\nThe distance the car will travel in', time, 'hours =', distance)

time = 10
distance = SPEED * time
print('The distance the car will travel in', time, 'hours =', distance)

time = 15
distance = SPEED * time
print('The distance the car will travel in', time, 'hours =', distance, end='\n\n')