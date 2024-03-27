# 19. Loan Payments Calculator

# Suppose you have taken out a loan for a certain 
# amount of money with a fixed monthly interest 
# rate and monthly payments, and you want to determine 
# the monthly payment amount necessary to pay off 
# the loan within a specific number of months. The 
# formula is as follows:

# P = (R * A) / 1 - (1 + R)^-M

# The terms in the formula are:

# • P is the payment amount per month.
# • R is the monthly interest rate, as a decimal (e.g., 2.5% 5 0.025).
# • A is the amount of the loan.
# • M is the number of months.

# Write a program that prompts the user to enter the 
# monthly interest rate as a percentage, 
# the loan amount, and the desired number of months. 
# The program should pass these values 
# to a function that returns the monthly payment 
# amount necessary. The program should

# prompts the user to enter the 
# monthly interest rate as a percentage, 
# the loan amount, and the desired number of months. 
def getInfo(prompt):
    number = float(input(prompt))
    while number < 0:
        number = float(input("Error. Enter a positive number: "))
    return number

def calculateMonthlyPayment(R, A, M):
    # P = (R * A) / 1 - (1 + R)^-M
    return (R * A) / (1 - pow((1 + R), -M))


def main():
    monthly_interest_rate = getInfo("Enter monthly interest rate as a percentage: ")
    loan_amount = getInfo("Enter loan amount: ")
    number_of_months = getInfo("Enter desired number of months: ")

    monthly_interest_rate = monthly_interest_rate / 100
    print(f"monthly interest rate = {monthly_interest_rate}")

    monthly_payment = calculateMonthlyPayment(
        monthly_interest_rate,
        loan_amount,
        number_of_months
    )

    print(f"Monthly payment = ${monthly_payment:,.2f}")

main()
