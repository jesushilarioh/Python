#
# 10. Tuition Increase 
#
# At one college, the tuitions for a full-time student is $ 8,000 per semester. It has been announced
# that the tuition will increase by 3 percent each year for the next 5 years. Write a program
# with a loop that displays the projected semester tuition amount for the next 5 years. 
# 
# 

TUITION_INCREASE = .03
YEARS = 5

variable_tuition = 8000.00
output = "Year\tIncrease\tTuition Cost\n" + \
         "------------------------------------\n"

increase = 0.0

for year in range(YEARS):

    if year == 0:
        output += format(year + 1) +    \
                  "\t$" + format(increase, '.2f') +   \
                  "\t\t$" + format(variable_tuition, '.2f') + "\n"

    else:
        increase = variable_tuition * TUITION_INCREASE
        variable_tuition = (variable_tuition * TUITION_INCREASE) + variable_tuition
        output += format(year + 1) +    \
                  "\t$" + format(increase, '.2f') +   \
                  "\t\t$" + format(variable_tuition, '.2f') + "\n"

output += "------------------------------------\n"

print(output)
