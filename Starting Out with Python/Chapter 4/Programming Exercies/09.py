#
# 9. Ocean Levels 
#
# Assuming the ocean's level is currently rising at about 1.6 millimeters per year, create an
# application that displays the number of millimeters that the ocean will have risen each year
# for the next 25 years. 
#
#
YEARS = 25
MILS_PER_YEAR = 1.6

output = "Years\tAmount Risen in Mils\n" + \
         "-----------------------\n"

amount_risen = 0

for year in range(YEARS):
    amount_risen = (year + 1) * 1.6  # += 1.6
    output += format(year + 1) + "\t" + format(amount_risen, '.2f') + "\n"

output += "-----------------------\n"

print(output)
