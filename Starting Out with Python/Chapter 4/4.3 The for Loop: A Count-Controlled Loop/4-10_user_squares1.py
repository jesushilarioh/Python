# This program uses a loop to display a
# table of numbers and their squares.

print('This program displays a list of numbers')
print('(starting at 1) and their squares.')
end = int(input('How high should I go? '))

print()
print('Number\tSquare')
print('--------------')

for number in range(1, end + 1):
    square = number**2
    print(number, '\t', square)
    

print('another version...')

# This program uses a loop to display a
# table of numbers and their squares.

print('This program displays a list of numbers')
print('(starting at 1) and their squares.')
end = int(input('How high should I go?'))

print()
print('Number\tSquare')
print('--------------')

for number in range(1, end + 1):
    square = number**2
    print(number, '\t', square)

