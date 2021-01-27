# This program demonstrates an infinite loop.
# Create a variable to control the loop.

keep_going = 'y'

while keep_going == 'y':
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    commission = sales * comm_rate

    print('The commission is $',
          format(commission, ',.2f'), sep='')