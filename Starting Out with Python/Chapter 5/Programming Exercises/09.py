# 9. Monthly Sales Tax
# A retail company must file a monthly sales 
# tax report listing the total sales for the month, 
# and the amount of state and county sales tax 
# collected. The state sales tax rate is 5 percent 
# and the county sales tax rate is 2.5 percent. 
# Write a program that asks the user to enter the 
# total sales for the month. From this figure, the 
# application should calculate and display the following:
# 
#   • The amount of county sales tax
#   • The amount of state sales tax
#   • The total sales tax (county plus state


# The state sales tax rate is 5 percent 
# and the county sales tax rate is 2.5 percent. 
STATE_SALES_TAX_RATE = .05 # 5%
COUNTY_SALES_TAX_RATE = .025 # 2.5%

def main():
    monthly_sales = getInfo("Enter total monthly sales: ")

    county_sales_tax = calculateCountySalesTax(monthly_sales)
    state_sales_tax = calculateStateSalesTax(monthly_sales)
    total_sales_tax = calculateTotalSalesTax(county_sales_tax, state_sales_tax)

    print(f"Total monthly sales = ${monthly_sales:,.2f}")
    print(f"County sales tax = ${county_sales_tax:,.2f}")
    print(f"State sales tax = ${state_sales_tax:,.2f}")
    print(f"Total sales tax = ${total_sales_tax:,.2f}")

def getInfo(prompt):
    user_input = int(input(prompt))

    while user_input < 0:
        user_input = int(input("Error. Enter a positive number: "))
        
    return user_input

def calculateCountySalesTax(monthly_sales):
    return monthly_sales * COUNTY_SALES_TAX_RATE

def calculateStateSalesTax(monthlu_sales):
    return monthlu_sales * STATE_SALES_TAX_RATE

def calculateTotalSalesTax(county_sales_tax, state_sales_tax):
    return county_sales_tax + state_sales_tax

main()