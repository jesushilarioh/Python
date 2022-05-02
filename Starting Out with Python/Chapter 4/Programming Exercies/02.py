# 2. Calories Burned 
# Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

from email import message


CALORIES_BURNED_PER_MINUTE = 4.2
num_burned_after_minutes = 0
message = 'number of calories burned after '

for minutes in range(5, 31, 5): 
    num_burned_after_minutes = minutes * CALORIES_BURNED_PER_MINUTE 
    message += format(minutes) + ' minutes = ' + format(num_burned_after_minutes)
    print(message)