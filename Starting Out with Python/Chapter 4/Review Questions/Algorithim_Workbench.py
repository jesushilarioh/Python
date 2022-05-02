# 1. Write a while loop that lets the user enter a number. The number should be multiplied by 10, and the result assigned to a variable named product. The loop should iterate as long as product is less than 100. 
# product = 0

# while product < 100:
#     userNumber = int(input("Enter a number: "))
#     product = userNumber * 10

#2. Write a while loop that asks the user to enter two numbers. The numbers should be added and the sum displayed. The loop should ask the user if he or she wishes to perform the operation again. If so, the loop should repeat, otherwise is should terminate.
# userChoice = 'y'

# while userChoice == 'y' or userChoice == 'Y':
#     number1 = int(input('enter number 1: '))
#     number2 = int(input("enter number 2: "))
#     sum = number1 + number2
#     print("sum =", sum)
#     userChoice = input('try again: ')

#3. Write a for loop that uses the range function to display all odd numbers between 1 and 100.
# for number in range(1, 100, 2):
#     print(number)

#4 Starting with a variable (text) containing an empty string, write a loop that prompts the user to type a word. Add the user's input to the end of (text) and then print the variable. The loop should repeat while the length of (text) is less than 10 characters. 
# text = ''

# while (len(text) < 10):
#     text += input('enter a letter: ')
#     print('text:', text)

#5 Write a loop that calculates the total of the following series of numbers: 1/30 + 2/29 + 3/28 ... 30/1
# denominator = 30
# total = 0

# for numerator in range(30):
#     # print(format(denominator) + '/' + format(numerator + 1))
#     total += denominator/(numerator + 1)
#     denominator -= 1

# print('total =', total)

#6 Rewrite the following statements using augmented assignments operators
# x = 39
# # a. x = x + 1
# x += 1

# # b. x = x * 2
# x *= 2

# # c. x = x / 10
# x /= 10

# # d. x = x - 100
# x -= 100

#7 Write a set of nested loops that displays the first ten values of the multiplication tables from 1 to 10. The code should print 100 lines in total, starting at "1 x 1 = 1" and ending with "10 x 10 = 100".
# for row in range(1, 11):
#     for col in range(1, 11):
#         print(format(row) + " x " + format(col) + " = " + format(row * col))

#8 Write code that prompts the user to enter a positive nonzero number and validates the input.
# userNumber = int(input("enter a positive nonzero number: "))
# while(userNumber % 10 == 0 or userNumber < 0):
#     userNumber = int(input("Error enter a positive nonzero number: "))

#9 Write code that prompts the user to enter a number in the range of 1 through 100 and validates the input.
userNumber =int(input("Enter a number between 1 and 100: "))

while(userNumber < 1 or userNumber > 100):
    userNumber = int(input("Error. Enter a number betwee 1 and 100: "))
