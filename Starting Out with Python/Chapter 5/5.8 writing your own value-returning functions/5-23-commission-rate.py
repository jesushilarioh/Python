# This program calculates a salesperson's
# pay at Make Your Own Music.
def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    comm_rate = determine_comm_rate(sales)
    pay = sales * comm_rate - advanced_pay

    print(f'The pay is ${pay:,.2f}.')

    if pay < 0:
        print('The Salesperson must reimburse')
        print('the company.')

def get_sales():
    return float(input('Enter the monthly sales: '))
    
def get_advanced_pay():
    print('Enter the amount of advanced pay, or')
    print('enter 0 if no advanced pay was given.')
    return float(input('Advanced pay: '))

def determine_comm_rate(sales):
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    return rate

main()