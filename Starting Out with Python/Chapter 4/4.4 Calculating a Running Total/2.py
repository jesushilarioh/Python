# This program calculates the sum of a series
# of numbers entered by the user.

MAX = 5

total = 0.0

print ('This program calculates the sum of')
print(MAX, 'numbers you will enter.')

for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number

print('The total is', total)

print()
print('another version...')

MAX = 5
total = 0.0

print('This program calculates the sum of')
print(MAX, 'numbers you will enter.')

for counter in range(MAX):
    number = int(input('Enter a number: '))
    total += number

print ('The total is', total)