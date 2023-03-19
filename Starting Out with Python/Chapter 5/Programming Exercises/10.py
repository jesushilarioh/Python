# 10. Feet to Inches
# One foot equals 12 inches. Write a function 
# named feet_to_inches that accepts a number 
# of feet as an argument and returns the number 
# of inches in that many feet. Use the function 
# in a program that prompts the user to enter a 
# number of feet then displays the number of 
# inches in that many feet.


def main():
    getFeetAndDisplayInches()

def getFeetAndDisplayInches():
    feet = getFloat("Enter number of feet: ")

    inches = feet_to_inches(feet)

    print(f"There are {inches:,.2f} inches in {feet} feet")

def feet_to_inches(feet):
    return feet * 12

def getFloat(prompt):
    user_input = int(input(prompt))

    while user_input < 0:
        user_input = int(input("Error. Enter a positive number: "))

    return user_input


main()
