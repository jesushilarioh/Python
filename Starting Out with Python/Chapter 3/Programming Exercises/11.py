# 11. Book Club Points
# Serendipity Booksellers has a book club that awards points 
# to its customers based on the number of books purchased each 
# month. The points are awarded as follows:

# • If a customer purchases 0 books, he or she earns 0 points.
# • If a customer purchases 2 books, he or she earns 5 points.
# • If a customer purchases 4 books, he or she earns 15 points.
# • If a customer purchases 6 books, he or she earns 30 points.
# • If a customer purchases 8 or more books, he or she earns 60 points.

# Write a program that asks the user to enter the number of books 
# that he or she has purchased this month, then displays the number of points awarded.

#INPUT
# 1. asks the user to enter the number of books 
# that he or she has purchased this month,
number_of_books = int(input("Enter the number of books: "))


#PROCESS
if number_of_books < 0:
    print("Error. Enter a positive number. Re-run program and try again.")
else:
    point_earned = 0
    #valid
    # 2. • If a customer purchases 0 books, he or she earns 0 points.
    if number_of_books >= 0 and number_of_books <= 1:
        point_earned = 0
    # • If a customer purchases 2 books, he or she earns 5 points.
    elif number_of_books >= 2 and number_of_books <= 3:
        point_earned = 5
    # • If a customer purchases 4 books, he or she earns 15 points.
    elif number_of_books >= 4 and number_of_books <= 5:
        point_earned = 15
    # • If a customer purchases 6 books, he or she earns 30 points.
    elif number_of_books >= 6 and number_of_books <= 7:
        point_earned = 30
    # • If a customer purchases 8 or more books, he or she earns 60 points.
    elif number_of_books >= 8:
        point_earned = 60

    # OUTPUT
    # 3. then displays the number of points awarded.
    print("You're awared", point_earned, "points.")