number = 0

def main():
    global number
    number = int(input('\n\nEnter a number: '))
    show_number()

def show_number():
    print(f'The number you entered is {number}.\n\n')

main()