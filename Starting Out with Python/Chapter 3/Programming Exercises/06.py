# 6. Magic Dates
#
# The date June 10, 1960, is special because when 
# it is written in the following format, the month 
# times the day equals the year:
#
# 6/10/60
#
# Design a program that asks the user to enter a 
# month (in numeric form), a day, and a two-digit 
# year. The program should then determine whether 
# the month times the day equals the year. If so, 
# it should display a message saying the date is 
# magic. Otherwise, it should display a message 
# saying the date is not magic.

# 1. asks the user to enter a 
# month (in numeric form), a day, and a two-digit 
# year.
month = int(input('Enter the month from 1 thru 12: '))
day = int(input('Enter the day from 1 thru 31: '))
year = int(input('Enter the year: '))

if (month * day) == year:
    print(month, '/', day, '/', year, ' IS magic.', sep='')
else:
    print(month, '/', day, '/', year, ' IS NOT magic.', sep='')
