# 16. Odd/Even Counter
# In this chapter, you saw an example of how to write an algorithm that determines 
# whether a number is even or odd. Write a program that generates 100 random numbers 
# and keeps a count of how many of those random numbers are even, and how many of 
# them are odd 

import random 

def main():

    total_count = 0
    total_even_numbers = 0
    total_odd_numbers = 0

    for index in range(100):
        number = random.randint(1, 100);

        if ((number % 2) == 0):
            total_even_numbers = total_even_numbers + 1
            print(f"EVEN: {number}")
        else:
            total_odd_numbers = total_odd_numbers + 1
            print(f"ODD : {number}")

        total_count = total_count + 1

    print(f"\nTotal count: {total_count}")
    print(f"Total even: {total_even_numbers}")
    print(f"Total odd: {total_odd_numbers}\n")


main()