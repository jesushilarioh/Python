# 7. Stadium Seating
# There are three seating categories at a stadium. 
# Class A seats cost $20, Class B seats cost 
# $15, and Class C seats cost $10. Write a program 
# that asks how many tickets for each class 
# of seats were sold, then displays the amount of 
# income generated from ticket sales
CLASS_A_PRICE = 20.00
CLASS_B_PRICE = 15.00
CLASS_C_PRICE = 10.00

def main():
# 1. asks how many tickets for each class of seats were sold
    ClassATickets = getInteger("How many tickets sold for Class A: ")
    ClassBTickets = getInteger("How many tickets sold for Class B: ")
    ClassCTickets = getInteger("How many tickets sold for Class C: ")

    totalSales = getTotalTicketSales(ClassATickets, ClassBTickets, ClassCTickets)

    print(f"Total nubmer of sales = ${totalSales:,.2f}")

# 2. displays the amount of income generated from ticket sales
def getTotalTicketSales(classA, classB, classC):
    classATotal = classA * CLASS_A_PRICE
    classBTotal = classB * CLASS_B_PRICE
    classCTotal = classC * CLASS_C_PRICE

    return classATotal + classBTotal + classCTotal

def getInteger(prompt):
    user_input = int(input(prompt))

    while user_input < 0:
        user_input = int(input("Enter a positive number: "))
    
    return user_input
        
main();

