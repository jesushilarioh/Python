#
# 6. Miles to Kilometers Table
# Write a program that displays a table of distances in miles and their equivalent distances in
# kilometers, rounded to 2 decimal places. One mile is equivalent to 1.60934 kilometers. The
# table should be generated using a loop, and should include values in 10 mile increments from
# 10 to 80. 
#
#

KILOMETERS = 1.60934

output = '\nMiles\t\tKilometers\n' \
         '-----------------------\n'

for mile in range(10, 81, 10):
    output += format(mile) + '\t\t' + format((mile * KILOMETERS), '.2f') + '\n'

output += '\n'

print(output)
