#
# 7. Pennies for Pay
# Write a program that calculates the amount of money a person would earn over a period of
# time if his or her salary is one penny the first day, two pennies the second day, and continues
# to double each day. The program should ask the user for the number of days. Display
# a table showing what the salary was for each day, then show the total pay at the end of the
# period. The output should be displayed in a dollar amount, not the number of pennies.
#
#
pennies = 0.01
number_of_days = int(input("Enter the number of days: "))
output = "Day\tPay\n" \
         "----------------------\n"
total_pay = 0.0
day_pay = 0.0

for day in range(number_of_days):

    if (day == 0): 
        day_pay = pennies
        output += format(day + 1) + "\t$" + format(day_pay, '.2f') + "\n"
        
    else: 
        day_pay = pennies
        output += format(day + 1) + "\t$" + format(day_pay, '.2f') + "\n"
        
    total_pay += day_pay
    pennies *= 2
    

output += "----------------------\n" \
          "Total pay = $" + format(total_pay, '.2f') + '\n'

print(output)