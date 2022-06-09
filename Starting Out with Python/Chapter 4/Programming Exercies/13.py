#
# 13. Population
#
# Write a program that predicts the approximate size of a population of organisms. The
# application should use text boxes to allow the user to enter the starting number of organisms,
# the average daily population increase (as a percentage), and the number of days the 
# organisms will be left to multiply. For example, assume the user enters the following values:
#
# Starting number of organisms: 2
# Average daily increase: 30%
# Number of days to multiply: 10
#
# The program should display the following table of data: 
#
#   Day Approx.     Population
#   1               2
#   2               2.6
#   3               3.38
#   4               4.39
#   5               5.7122
#   6               7.42586
#   7               9.653619
#   8               12.5497
#   9               16.31462
#   10              21.209
#
#

starting_number_of_organisims = int(input("\nStarting number of organisms: "))

while starting_number_of_organisims < 0:
    starting_number_of_organisims = int(input("Error: Enter a positive number: "))
    

average_daily_increase = float(input("Average daily increase: "))

while average_daily_increase < 0:
    average_daily_increase = float(input("Error: enter a positive number: "))


average_daily_increase /= 100

number_of_days_to_multiply = int(input("Number of days to multiply: "))

while number_of_days_to_multiply < 0:
    number_of_days_to_multiply = int(input("Error. Enter a positive number: "))


output = "\nDay Approx.\tPopulation\n" + \
         "-----------------------------------\n"

population = starting_number_of_organisims

for day in range(number_of_days_to_multiply):

    if day == 0:
        output += format(day + 1) + "\t\t" + format(population) + "\n"

    else:
        population += (population * average_daily_increase)
        output += format(day + 1) + "\t\t" + format(population) + "\n"

output += "-----------------------------------\n"

print(output)