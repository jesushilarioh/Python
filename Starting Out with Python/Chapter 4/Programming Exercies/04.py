#
# 4. Distance Traveled
# The distance a vehicle travels can be calculated as follows:
# 
# distance = speed x time
# 
# For example, if a train travels 40 miles per hour for three
# hours, the distance traveled is 120 miles. Write a program
# that asks the user for the speed of a vehicle (in miles per hour)
# and the number of hours it has traveled. It should then use a loop
# to display the distance the vehicle has traveled for each
# hour of that time period. Here is an example of the desired 
# output:
# 
# What is the speed of the vehicle in mph? 40
# How many hours has if traveled? 3 
# Hour      Distance Traveled
# ------------------------------
# 1         40
# 2         80
# 3         120
#  

speed = int(input("\nEnter the speed: "))  
while speed < 0:
      speed = int(input("Error: Enter a positive number: "))  
      
hours = int(input("Enter hours traveled: "))  
while hours < 0:
      hours = int(input("Error: Enter a positive number: "))  
      
distance = 0

output = "\nHour     Distance Traveled\n"  \
         "--------------------------\n"
      
for hour in range(hours):
    distance = speed * (hour + 1)

    output += format(hour + 1) + "       " + \
              format(distance) + "\n"

print(output)