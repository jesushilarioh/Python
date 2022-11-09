# 4. Automobile Costs
# Write a program that asks the user to enter the monthly costs for the following expenses 
# incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and 
# maintenance. The program should then display the total monthly cost of these expenses, 
# and the total annual cost of these expenses.

def get_float(string):
    return float(input(string))

def get_annual_cost(number):
    return number * 3

def main():

    print("Enter monthly costs.")
    loan_payment = get_float("Loan payment: ")
    insurance = get_float("Insurance: ")
    gas = get_float("Gas: ")
    oil = get_float("Oil: ")
    tires = get_float("Tires: ")
    maintenance = get_float("Maintenance: ")

    total_monthly_cost = loan_payment + \
                         insurance + \
                         gas + \
                         oil + \
                         tires + \
                         maintenance

    total_annual_cost = get_annual_cost(total_monthly_cost)

    print(f"Total monthly = ${total_monthly_cost:,.2f}")
    print(f"Total annual cost = ${total_annual_cost:,.2f}")

main()         

