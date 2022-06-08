#
# 15. Write a program that uses nested loops to draw this pattern:
#
#   ##
#   # #
#   #  #
#   #   #
#   #    #
#   #     #
#
#

SIZE = 7

output = "\n"

for row in range(SIZE):
    output += "#"
    
    for column in range(row + 1):
        output += " "

    output += "#\n"

print(output)