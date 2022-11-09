# 5. Property Tax
# A county collects property taxes on the assessment value of property, which is 60 percent of 
# the property’s actual value. For example, if an acre of land is valued at $10,000, its assessment 
# value is $6,000. The property tax is then 72¢ for each $100 of the assessment value. 
# The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the 
# actual value of a piece of property and displays the assessment value and property tax

ASSESSMENT_VALUE_PERCENTAGE = .60
CENTS = .72
DOLLARS = 100


def calculate_assessment_value(actual_home_value):
    return actual_home_value * ASSESSMENT_VALUE_PERCENTAGE

def calculate_property_tax(assessment_value):
    return (assessment_value / DOLLARS) * CENTS

def main():

    actual_home_value = float(input("Enter actual home value: "))
    assessment_value = calculate_assessment_value(actual_home_value)
    property_tax = calculate_property_tax(assessment_value)

    print(f"Actual value = ${actual_home_value:,.2f}")
    print(f"Assessment value = ${assessment_value:,.2f}")
    print(f"Property tax = ${property_tax:,.2f}")

main()
