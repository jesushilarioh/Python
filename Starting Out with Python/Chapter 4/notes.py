# the range function in a for loop with the 
# iterable being [0, 1, 2, 3, 4]. 
# An iterable is an object that is similar to a list.
# It contains a sequence of values 
# that can be iterated over with something 
# like a loop.
# for num in range(5):
#     print(num)

# same as
# for num in [0, 1, 2, 3, 4]:
#     print(num)

# The range function with 2 arguments in a for loop
for num in range(1, 5):
    print(num)

# The range function with 3 arguments in a for loop
# the 3rd argument being the step value
for num in range(1, 10, 2):
    print(num)

# The range function to generate a sequence of numbers
# that go from highest to lowest.
for num in range(100, 90 - 1, -1):
    print(num, '\t', num**2)