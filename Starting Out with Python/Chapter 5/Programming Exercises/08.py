# A painting company has determined that for every 
# 112 square feet of wall space, one gallon of paint 
# and eight hours of labor will be required. The 
# company charges $35.00 per hour for labor. Write 
# a program that asks the user to enter the square 
# feet of wall space to be painted and the price 
# of the paint per gallon. The program should 
# display the following data:
#
#   • The number of gallons of paint required
#   • The hours of labor required
#   • The cost of the paint
#   • The labor charges
#   • The total cost of the paint job
CHARGE_PER_HOUR = 35.00
WALL_SPACE_PER_GALLON = 112
HOURS_PER_GALLON = 8

def main():
    square_ft_wall_space = getFloat("Enter number of square feet of wall space: ")
    price_of_paint_per_gallon = getFloat("Enter the price of paint per gallon: ")

    gallons_needed = getTotalGallons(square_ft_wall_space)
    labor_hours_needed = getTotalLaborHours(square_ft_wall_space)
    cost_of_paint = getTotalCostOfPaint(gallons_needed, price_of_paint_per_gallon)
    labor_charges = getLaborCharge(labor_hours_needed)
    total_cost = cost_of_paint + labor_charges

    print(f"Number of gallons of paint required = {gallons_needed:,.2f}")
    print(f"Hours of labor required = {labor_hours_needed:,.2f}")
    print(f"Cost of paint = ${cost_of_paint:,.2f}")
    print(f"Labor charges = ${labor_charges:,.2f}")
    print(f"Total cost of paint job = ${total_cost:,.2f}")
    
def getFloat(prompt):
    user_input = float(input(prompt))

    while user_input < 0:
        user_input = float(input("Error. Enter positive number: "))

    return user_input

def getTotalGallons(totalWallSpace):
    return totalWallSpace / WALL_SPACE_PER_GALLON

def getTotalLaborHours(totalWallSpace):
    return (totalWallSpace / WALL_SPACE_PER_GALLON) * 8

def getTotalCostOfPaint(totalCost, totalGallons):
    return totalCost * totalGallons

def getLaborCharge(hours_needed):
    return hours_needed * CHARGE_PER_HOUR

main()