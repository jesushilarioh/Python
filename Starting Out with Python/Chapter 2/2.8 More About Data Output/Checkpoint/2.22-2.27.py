# 2.22 How do you suppress the print function’s ending newline?
print("One", end=' ')
print("Two", end=' ')
print("Three")

# 2.23 How can you change the character that is automatically displayed between
# multiple items that are passed to the print function?
print("One", "Two", "Three", sep='____')

# 2.24 What is the '\n' escape character?
#ANSWER: the '\n' escape character creates a newline
print('One\nTwo\nThree')

# 2.25 What does the + operator do when it is used with two strings?
# ANSWER: The + operator concatinates two strings
print('String 1 ' + 'and' + ' String 2')

# 2.26 What does the statement print(format(65.4321, '.2f')) display? 
# ANSWER: 65.43
print(format(65.4321, '.2f'))

# 2.27 What does the statement print(format(987654.129, ',.2f')) display?
# ANSWER: 987,654.13
print(format(987654.129, ',.2f'))