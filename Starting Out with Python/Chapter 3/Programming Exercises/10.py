# 10. Money Counting Game
#
# Create a change-counting game that gets the user to 
# enter the number of coins required to make exactly 
# one dollar. The program should prompt the user to 
# enter the number of pennies, nickels, dimes, and 
# quarters. If the total value of the coins entered 
# is equal to one dollar, the program should congratulate 
# the user for winning the game. Otherwise, the program 
# should display a message indicating whether the amount 
# entered was more than or less than one dollar.

# INPUT
# 1. prompt the user to 
#   enter the number of pennies, nickels, dimes, and 
#   quarters.
PENNY = .01
NICKEL = .05
DIME = .10
QUARTER = .25

pennies = float(input("Enter number of pennies: "))
nickels = float(input("Enter number of nickels: "))
dimes = float(input("Enter number of dimes: "))
quarters = float(input("Enter number of quarters: "))

pennies *= PENNY # pennies = pennies * PENNY
nickels *= NICKEL # nickels = nickels * NICKEL
dimes *= DIME # dimes = dimes * DIME
quarters *= QUARTER # quarters = quarters * QUARTERS

# print("pennies =", pennies)
# print("nickels =", nickels)
# print("dimes =", dimes)
# print("quarters =", quarters)

total = pennies + nickels + dimes + quarters

if_won_or_lost = ""

# PROCESS
if total == 1.00:
    if_won_or_lost = "Won"

# 2. If the total value of the coins entered 
#   is equal to one dollar, the program should congratulate 
#   the user for winning the game.
else:
    if_won_or_lost = "Lost"
    if total > 1.00:
        print("The amount entered is greater than 1 dollar.")
    else:
        print("The amount entered is less than 1 dollar.")
    # LOst

# 3. Otherwise, the program 
# should display a message indicating whether the amount 
# entered was more than or less than one dollar.

# OUTPUT
print("You", if_won_or_lost)
print("Your total was", total)