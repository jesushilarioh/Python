#.3
# Write a for loop that uses the range function to display all
# odd numbers between 1 and 100.
message = ""

for oddNumber in range(1, 100, 2):
    message += format(oddNumber) + "\n"

print(message)