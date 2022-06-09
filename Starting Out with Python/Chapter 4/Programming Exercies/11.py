#
# 11. Sleep Debt 
#
# A "sleep debt" represents the difference between a person's desirable and actual amount of
# sleep. Write a program that prompts the user to enter how many hours he or she slept each
# day over a period of 7 days. Using 8 hours per day as the desirable amount of sleep, determine
# his or her sleep debt by calculating the total hours of sleep they got over the seven-day
# period and subtracting that from the total hours of sleep he or she should have got. If the
# user does not have a sleep debt, display a message expressing your jealousy. 
#
#

DAYS = 7
REQUIRED_SLEEP_AMOUNT = DAYS * 8

hours_slept = 0.0
total_sleep_hours = 0.0

for day in range(DAYS):
    hours_slept = float(input("How many sleep hours on day " + format(day + 1) + "? "))

    while hours_slept < 0:
        hours_slept = float(input("Error: Enter a positive number: "))
        
    total_sleep_hours += hours_slept

sleep_debt = REQUIRED_SLEEP_AMOUNT - total_sleep_hours

output = "\nTotal sleep debt = " + format(sleep_debt, '.2f') + "\n"

if sleep_debt > 0:
    output += "\nYou need more sleep!!\n"
else:
    output += "\nYou are sleeping well!!\n"

print(output)
