# 3. How Much Insurance?
# Many financial experts advise that property owners should insure their homes or buildings 
# for at least 80 percent of the amount it would cost to replace the structure. Write a program 
# that asks the user to enter the replacement cost of a building, then displays the minimum 
# amount of insurance he or she should buy for the property.

# 80 percent of the amount
INSURE_PERCENTAGE = .80

def minimum_replacement_cost(num):
    return num * INSURE_PERCENTAGE

# asks the user to enter the replacement cost of a building,
def main():
    
    replacement_cost = float(input("Enter replacement cost: "))
    print(f'Replacement cost = ${minimum_replacement_cost(replacement_cost):,.2f}')

main()

# then displays the minimum 
# amount of insurance he or she should buy for the property.