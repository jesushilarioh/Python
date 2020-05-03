#
# 2. Sales Prediction
#
# A company has determined that its annual profit 
# is typically 23 percent of total sales. Write a 
# program that asks the user to enter the projected 
# amount of total sales, then displays the profit 
# that will be made from that amount.
#
# Hint: Use the value 0.23 to represent 23 percent.
#

PROFIT_PERCENTAGE = .25
total_sales = float(input('\nEnter projected total sales amout: $'))
annual_profit = total_sales * PROFIT_PERCENTAGE
print('Total profit made = $' + format(annual_profit, ',.2f') + '\n')