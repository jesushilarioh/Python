# 7. Prime Numbers
# A prime number is a number that is only evenly divisible 
# by itself and 1. For example, the number 5 is prime 
# because it can only be evenly divided by 1 and 5. The 
# number 6, however, is not prime because it can be 
# divided evenly by 1, 2, 3, and 6. Write a Boolean function 
# named is_prime which takes an integer as an argument and 
# returns true if the argument is a prime number, or 
# false otherwise. Use the function in a program that 
# prompts the user to enter a number then displays a 
# message indicating whether the number is prime. 

# TIP: Recall that the % operator divides one number by 
# another and returns the remainder of the division. In 
# an expression such as num1 % num2, the % operator will 
# return 0 if num1 is evenly divisible by num2.



# Write a Boolean function 
# named is_prime which takes an integer as an argument and 
# returns true if the argument is a prime number, or 
# false otherwise.
def is_prime(number):

    isPrime = 0

    for index in range(1, (number + 1)):
        if number % index == 0:
            isPrime = isPrime + 1

    if isPrime == 2:
        return True
    else:
        return False

# Use the function in a program that 
# prompts the user to enter a number then displays a 
# message indicating whether the number is prime. 
def main():
    user_number = int(input("Enter a number: "))

    while user_number < 0:
        user_number = int(input("Error. Enter a positive number: "))

    if is_prime(user_number):
        print("Your number is PRIME")
    else:
        print("Your number is NOT PRIME")

main()