#
# .3
# Write a program that asks the user to enter the number
# of times that they have run around a racetrack, and then
# uses a loop to prompt them to enter the lap time for
# each of their laps. When the loop finishes, the program 
# should display the time of their fastest lap, the time of
# their slowest lap, and their average lap time.
#

fastestLapTime = 0.0
slowestLapTime = 0.0
averageLapTime = 0.0
userLapTime = 0.0
totalLapTime = 0.0


# 1. asks the user to enter the number
# of times that they have run around a racetrack
numberAroundTrack = int(input("How many times around track? "))

# 2. uses a loop to prompt them to enter the lap time for
# each of their laps.
for lapTime in range(numberAroundTrack):

    userLapTime = float(input("Enter lap time for lap #" + format(lapTime + 1) + " "))

    if userLapTime > fastestLapTime:
        fastestLapTime = userLapTime
        
    if userLapTime < slowestLapTime:
        slowestLapTime = userLapTime

    totalLapTime += userLapTime

averageLapTime = totalLapTime / numberAroundTrack

# 3.  When the loop finishes, the program 
# should display the time of their fastest lap, the time of
# their slowest lap, and their average lap time.
output = "Fastest lap = " + format(fastestLapTime) + "\n"  \
          "Slowest lap = " + format(slowestLapTime) + "\n"  \
          "Average lap time = " + format(averageLapTime, '.2f') + ". "

print(output)