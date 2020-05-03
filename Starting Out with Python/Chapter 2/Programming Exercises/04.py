# 
# 4. Total Purchase
# 
# A customer in a store is purchasing five items. 
# Write a program that asks for the price of each 
# item, then displays the subtotal of the sale, the 
# amount of sales tax, and the total. Assume the 
# sales tax is 7 percent.
# 

SALES_TAX = .07

item1 = float(input('\nEnter the price for item 1 $'))
item2 = float(input('Enter the price for item 2 $'))
item3 = float(input('Enter the price for item 3 $'))
item4 = float(input('Enter the price for item 4 $'))
item5 = float(input('Enter the price for item 5 $'))

subtotal =  float(item1 + item2 + item3 + \
                  item4 + item5)
            
total_sales_tax = subtotal * SALES_TAX

total = subtotal + total_sales_tax

print('\nTotal = $', format(total, ',.2f'), sep='', end='\n\n')