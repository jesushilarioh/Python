# 19a. Future Value 

# Suppose you have a certain amount of money in a savings 
# account that earns compound monthly interest, and you 
# want to calculate the amount that you will have after 
# a specific number of months. The formula, which is known 
# as the future value formula, is:

# F = P x (1 + i)^t

# The terms in the formula are as follows:

# • F is the future value of the account after the specified time period.
# • P is the present value of the account.
# • i is the monthly interest rate.
# • t is the number of months.

# Write a program that prompts the user to enter the 
# account’s present value, monthly interest rate, and 
# the number of months that the money will be left in 
# the account. The program should pass these values 
# to a function named futureValue that returns the 
# future value of the account, after the specified 
# number of months. The program should display the 
# account’s future value.


# prompts the user to enter the 
# account’s present value, monthly interest rate, and 
# the number of months that the money will be left in 
# the account.
def get_info(prompt):
    number = float(input(prompt))
    while number < 0:
        number = float(input("Error. Enter a positive number: "))
    return number

def main():
    account_present_value = get_info("Enter account's present value: ")
    monthly_interest_rate = get_info("Enter monthly interest rate: ")
    # monthly_interest_rate = monthly_interest_rate * .01
    number_of_months = get_info("Enter number of months that the money will be left in account: ")

    print(f"Future value = ${future_value(account_present_value, monthly_interest_rate, number_of_months):,.2f}")

# pass these values 
# to a function named futureValue that returns the 
# future value of the account, after the specified 
# number of months.
def future_value(P, i, t):
    # F = P x (1 + i)^t
    return P * pow((1 + i), t)


# The program should display the 
# account’s future value.

main()