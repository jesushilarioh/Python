# 6. Payment Instalments
# 
# Write a program that asks the user to enter 
# the amount of a purchase and the desired 
# number of payment instalments. The program 
# should add 5 percent to the amount to get 
# the total purchase amount, and then divide 
# it by the desired number of instalments, then
# display messages telling the user the total 
# amount of the purchase and how much each
# installment will cost.
# 
purchase_amount = float(input('Enter the amount of purchase: $'))
number_of_installments = int(input('Enter number of payment installments: '))

PERCENTAGE = .05
total_purchase_amount = (purchase_amount * PERCENTAGE) + purchase_amount
installment_amount = total_purchase_amount / number_of_installments

print('\nPurchase amount = $', format(purchase_amount, ',.2f'), sep='')
print('Number of installments =', number_of_installments)
print('Total purchase amount = $', format(total_purchase_amount, ',.2f'), sep='')
print('Installment amount = $', format(installment_amount, ',.2f'), sep='', end='\n\n')