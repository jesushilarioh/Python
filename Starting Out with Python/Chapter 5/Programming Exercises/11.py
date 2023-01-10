# 11. Addition Test
# Write a program that generates printable 
# addition tests. The tests should consist of 
# 5 questions which present a simple addition 
# question in the following format, where the 
# question number goes from 1 to 5, and num1 and 
# num2 are randomly generated numbers between 1 and 10:
#  Question 1
#  num1 + num2 = _____
# The program should simply display the 5 questions; 
# it should not prompt the user for any input.
import random

def main():

    for count in range(5):
        num1 = random.randint(1, 5)
        num2 = random.randint(1, 5)
        print(f"{num1} + {num2} = ____")

main()
