# This program converts cup fluid ounces.

def main():
    # display the intro screen.
    intro()
    # Get the number of cups.
    cups_needed = int(input('Enter the number of cups: '))
    # Convert the cups to ounces.
    cups_to_ounces(cups_needed)

def intro():
    print('\nThis program converts measurements')
    print('in cups to fluid ounces. For your')
    print('reference the formula is: ')
    print('1 cup = 8 fluid ounces')
    print()

def cups_to_ounces(cups):
    ounces = cups * 8
    print('\nThat converts to', ounces, 'ounces.\n')

main()

