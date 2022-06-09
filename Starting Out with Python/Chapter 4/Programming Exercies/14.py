#
# 14. Write a program that uses nested loops to draw this pattern: 
#
#   *******
#   ******
#   *****
#   ****
#   ***
#   **
#   *
#
#

SIZE = 8

output = "\n"

for rows in range(SIZE, 0, -1):

    for columns in range(rows):
        
        output += "#"
    
    output += "\n"

print(output)

