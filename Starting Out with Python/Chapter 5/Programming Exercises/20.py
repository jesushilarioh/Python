# 20. Random Number Guessing Game

# Write a program that generates a random 
# number in the range of 1 through 100, 
# and asks the user to guess what the number is. 
# If the user’s guess is higher than the random number, 
# the program should display “Too high, try again.” 
# If the user’s guess is lower 
# than the random number, the program should 
# display “Too low, try again.” If the user 
# guesses the number, the application should 
# congratulate the user and generate a new random 
# number so the game can start over.

# Optional Enhancement: Enhance the 
# game so it keeps count of the number of guesses that 
# the user makes. When the user correctly guesses 
# the random number, the program should 
# display the number of guesses.

import random

def main():

    random_number = random.randint(1, 100)
  
    user_guess = int(input("Select a number in the range of 1 through 100: "))
    while user_guess < 1 and user_guess > 100:
        user_guess = int(input("Error. Select a number in the range of 1 through 100: "))

    # keeps count of the number of guesses that 
    # the user makes. 
    number_of_guesses = 1

    while user_guess != random_number:

        # If the user’s guess is higher than the random number, 
        # the program should display “Too high, try again.” 

        # If the user’s guess is lower 
        # than the random number, the program should 
        # display “Too low, try again.” 

        # If the user 
        # guesses the number, the application should 
        # congratulate the user and generate a new random 
        # number so the game can start over.

    

    # When the user correctly guesses 
    # the random number, the program should 
    # display the number of guesses.