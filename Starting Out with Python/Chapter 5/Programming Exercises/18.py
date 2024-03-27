# 18. Prime Number List
# This exercise assumes that you have already 
# written the is_prime function in Programming 
# Exercise 17. Write another program that 
# displays all of the prime numbers from 1 to 100. 
# The program should have a loop that calls 
# the is_prime function


def is_prime(number):

    isPrime = 0

    for index in range(1, (number + 1)):
        if number % index == 0:
            isPrime = isPrime + 1

    if isPrime == 2:
        return True
    else:
        return False
    
# Write another program that 
# displays all of the prime numbers from 1 to 100. 
# The program should have a loop that calls 
# the is_prime function
def main():
    RANGE = 100
    print(f"Here are all the prime number to 100: ")

    for index in range (RANGE):
        if is_prime(index + 1):
            print(f"{index + 1} PRIME")
        else:
            print(index + 1)

main()