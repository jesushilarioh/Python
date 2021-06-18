# 4.1 What is a repetition structure?
# A structure that repeats the same portion of code as many times as necessary.

# 4.2 What is a condition-controlled loop?
# A condition-controlled loop uses a true/false condition to control the number of times that it repeats.
# A true/false condition controls the number of times the condition-controlled loop will iterate.

# 4.3 What is a count-controlled loop?
# A count-controlled loop repeats a specific number of times.
# A specific number will controll how many times the count-controlled loop will iterate/repeat.

# 4.4 What is a loop iteration?
# An iteration is each execution of the body of a loop.

# 4.5 Does the while loop test its condition before or after it performs an iteration?
# The while loop tests its condition after it's initial first iteration.

# 4.6 How many times will 'Hello World' be printed in the following program?
count = 10
while count < 1:
    print('Hello World')
# 'Hello World' will NOT be printed at all, because count is intially set to 10. 
# Because count is intially set to 10, the program will NOT output 'Hello World'.

# 4.7 What is an infinite loop?
# An infinite loop is a loop that has no way of stopping. 

# 4.8 Rewrite the following code so it calls the range function instead of using the list
# [0, 1, 2, 3, 4, 5]
print('\n4.8')
print('------')

for x in range(6):
    print('I love to program!')

# 4.9 What will the following code display?
print('\n4.9')
print('------')

for number in range(6):
    print(number)
# 0
# 1
# 2
# 3
# 4
# 5

# 4.10 What will the following code display?
print('\n4.10')
print('------')

for number in range(2, 6):
    print(number)
# 2
# 3
# 4
# 5

# 4.11 What will the following code display?
print('\n4.11')
print('------')

for number in range(0, 501, 100):
    print(number)
# 0
# 100
# 200
# 300
# 400
# 500

# 4.12 What will the following code display?
print('\n4.12')
print('------')

for number in range(10, 5, -1):
    print(number)
# 10
# 9
# 8
# 7
# 6

# 4.13 What is an accumulator?
# A variable used to keep a running total.
# A variable that accumulates as it's corresponding loop persists...
# A variable that is used to accumulate the total of the numbers.

# 4.14 Should an accumulator be initialized to any specific value?
#      Why or why not?
# Yes. 0. If a value is not initially assigned to an accumulator variable,
# the accumulator will start an a random number give by memory. Thus, it
# may not contain the correct total when the loop finishes.

# 4.15 What will the following code display?
print('\n4.15')
print('------')
total = 0
for count in range(1, 6):
    total = total + count
print(total) # 15

# 4.16 What will the following code display?
print('\n4.16')
print('------')
number1 = 10
number2 = 5
number1 = number1 + number2
print(number1)  # 15
print(number2)  # 5

# 4.17 Rewrite the following statements using augmented assignment operators:
print('\n4.17')
print('------')
# a) quantity = quantity + 1 
quantity = 0
quantity += 1
# b) days_left = days_left - 5 
days_left = 0
days_left =- 5
# c) price = price * 10
price = 0
price *= 10
# d) price = price / 2
price /= 2

