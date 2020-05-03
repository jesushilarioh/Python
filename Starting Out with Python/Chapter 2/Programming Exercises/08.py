# 8. Tip, Tax, and Total
# 
# Write a program that calculates the 
# total amount of a meal purchased at a 
# restaurant. The program should ask the 
# user to enter the charge for the food, 
# then calculate the amounts of a 18 percent 
# tip and 7 percent sales tax. Display each 
# of these amounts and the total.
# 

charge_for_food = float(input('\nEnter charge for food: $'))

TIP_PERCENTAGE = .18
SALES_TAX = .07

tip = (charge_for_food * TIP_PERCENTAGE)
sales_tax = (charge_for_food * SALES_TAX)
grand_total = charge_for_food + tip + sales_tax

print('\nCharge for food = $', format(charge_for_food, ',.2f'), sep='')
print('Tip = $', format(tip, ',.2f'), sep='')
print('Sales tax = $', format(sales_tax, ',.2f'), sep='')
print('Grand total = $', format(grand_total, ',.2f'), sep='', end='\n\n')