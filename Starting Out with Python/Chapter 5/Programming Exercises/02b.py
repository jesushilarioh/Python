# 2. Sales Tax Program Refactoring 
#
# Programming Exercise #6 in Chapter 2 was the 
# Sales Tax program. For that exercise, you were 
# asked to write a program that calculates and 
# displays the county and state sales tax on a 
# purchase. If you have already written that 
# program, redesign it so the subtasks are in 
# functions. If you have not already written that 
# program, write it using functions.
#
def main():
    STATE_SALES_TAX = .05
    COUNTY_SALES_TAX = .025

    user_amount = float(input("Enter amount of purchase: "))

    total_state_tax = calculate_sales_tax(user_amount, STATE_SALES_TAX)
    total_county_tax = calculate_sales_tax(user_amount, COUNTY_SALES_TAX)

    total_tax = calculate_sum(total_state_tax, total_county_tax)
    total_of_sale = calculate_sum(user_amount, total_tax)

    display_info('Amount of purchase ', user_amount)
    display_info('State sales tax    ', total_state_tax)
    display_info('County sales tax   ', total_county_tax)
    display_info('Total sales tax    ', total_tax)
    display_info('Total of sale      ', total_of_sale)

def display_info(output, number):
    print(f'{output} = ${number:,.2f}')

def calculate_sales_tax(amount, sales_tax):
    return amount * sales_tax

def calculate_sum(number1, number2):
    return number1 + number2
    
main()
