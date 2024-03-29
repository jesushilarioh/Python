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
userLapTime    = 0.0
totalLapTime   = 0.0

numberAroundTrack = int(input("How many times around the track? "))

while numberAroundTrack < 0:
    numberAroundTrack = int(input("Error. Enter a positive number: "))

for lapTime in range(numberAroundTrack):

    userLapTime = float(input("Enter lap time for lap #" + format(lapTime + 1) + " "))

    while userLapTime < 0:
        userLapTime = float(input("Error. Enter a positive number: "))

    if lapTime == 0:
        fastestLapTime = slowestLapTime = userLapTime

    else: 
        if userLapTime > fastestLapTime:
            fastestLapTime = userLapTime
        
        elif userLapTime < slowestLapTime:
            slowestLapTime = userLapTime

    totalLapTime += userLapTime

averageLapTime = totalLapTime / numberAroundTrack

output = "\nFastest lap      = " + format(fastestLapTime) + "\n"  \
         "Slowest lap      = " + format(slowestLapTime) + "\n"  \
         "Average lap time = " + format(averageLapTime) + ".\n"

print(output)