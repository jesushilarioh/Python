# 
# 12. Stock Transaction Program
# Last month, Joe purchased some stock in Acme Software, 
# Inc. Here are the details of the purchase:
# 
# • The number of shares that Joe purchased was 2,000.
# • When Joe purchased the stock, he paid $40.00 per share.
# • Joe paid his stockbroker a commission that amounted to 
#   3 percent of the amount he paid for the stock.
# 
# Two weeks later, Joe sold the stock. Here are the details 
# of the sale:
# 
# • The number of shares that Joe sold was 2,000.
# • He sold the stock for $42.75 per share.
# • He paid his stockbroker another commission that amounted 
#   to 3 percent of the amount he received for the stock.
# 
# Write a program that displays the following information:
# 
# • The amount of money Joe paid for the stock.
# • The amount of commission Joe paid his broker when he 
#   bought the stock.
# • The amount for which Joe sold the stock.
# • The amount of commission Joe paid his broker when he 
#   sold the stock.
# • Display the amount of money that Joe had left when he 
#   sold the stock and paid his broker (both times). If 
#   this amount is positive, then Joe made a profit. If 
#   the amount is negative, then Joe lost money.

STOCKBROKER_COMMISSION = .03

shares_sold = shares_purchased = 2000
price_per_share = 40.00

amount_paid_for_stock = shares_purchased * price_per_share
print('\nAmount of money paid for the stock = $', 
       format(amount_paid_for_stock, ',.2f'), 
       sep='')

commission_paid_when_bought = amount_paid_for_stock * STOCKBROKER_COMMISSION
print('Amount of commission paid to broker when Joe bought the stock = $', 
       format(commission_paid_when_bought, ',.2f'),
       sep='')

price_per_share = 42.75

amount_stock_sold_for = shares_sold * price_per_share
print('Amount for which Joe sold the stock = $', 
       format(amount_stock_sold_for, ',.2f'),
       sep='')

commission_paid_when_sold = amount_stock_sold_for * STOCKBROKER_COMMISSION
print('Amount of commission paid to broker when Joe sold the stock = $',
       format(commission_paid_when_sold, ',.2f'),
       sep='')

total_amount_left = amount_stock_sold_for - \
                   (commission_paid_when_bought + \
                    commission_paid_when_sold)

print('\nTotal leftover =', 
      format(total_amount_left, ',.2f'), 
      '\nJoe made a profit.\n')