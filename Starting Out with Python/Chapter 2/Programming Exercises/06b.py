#
# 6. Sales Tax
# 
# Write a program that will ask the user 
# to enter the amount of a purchase. The 
# program should then compute the state 
# and county sales tax. Assume the state 
# sales tax is 5 percent and the county 
# sales tax is 2.5 percent. The program 
# should display the amount of the purchase, 
# the state sales tax, the county sales 
# tax, the total sales tax, and the total 
# of the sale (which is the sum of the 
# amount of purchase plus the total sales 
# tax).
#
# Hint: Use the value 0.025 to represent 
# 2.5 percent, and 0.05 to represent 
# 5 percent.
#

STATE_SALES_TAX = .05
COUNTY_SALES_TAX = .025

user_amount = float(input("Enter amount of purchase: "))

total_state_tax = user_amount * STATE_SALES_TAX
total_county_tax = user_amount * COUNTY_SALES_TAX

total_tax = total_state_tax + total_county_tax

total_of_sale = user_amount + total_tax

print(f'Amount of purchase = ${user_amount:,.2f}')
print(f'State sales tax    = ${total_state_tax:,.2f}')
print(f'County sales tax   = ${total_county_tax:,.2f}')
print(f'Total sales tax    = ${(total_tax):,.2f}')
print(f'Total of sale      = ${total_of_sale:,.2f}')