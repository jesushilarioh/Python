# This program uses the return value of a function
def main():
    first_age = int(input('Enter your age: '))
    second_age = int(input('Enter your best friend\'s age: '))
    total = sum(first_age, second_age)
    print(f'Together you are {total} years old.')

def sum(num1, num2):
    result = num1 + num2
    return result

main()
