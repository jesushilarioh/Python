# This program demonstrates the None keyword.

def main():
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    quotient = divide(num1, num2)

    if quotient is None:
        print('Cannot divide by zero.')
    else:
        print(f'{num1} divide by {num2} is {quotient}.')

    print(type(quotient))

def divide(num1, num2):
    if num2 == 0:
        result = None
    else:
        result = num1 / num2
    return result

main()