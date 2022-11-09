# Algorithm Workbench

# 1. Write a function named shout. The function 
# should accept a string argument and display it 
# in uppercase with an exclamation mark concatenated 
# to the end.
def shout(str):
    print(f"{str.upper()}")

shout("hello, how's it going!?")


# 2. Examine the following function header, then 
# write a statement that calls the function, 
# passing 12 as an argument.
def show_value(quantity):
    print(f'quantity = {quantity:.2f}')

show_value(13)


# 3. Look at the following function header:
def my_function(a, b, c):
    return a + b + c

# Now look at the following call to my_function:
print(f'sum = {my_function(3, 2, 1):.2f}')

# When this call executes, what value will be 
# assigned to a? 
# a = 3
# What value will be assigned to b? 
# b = 2
# What value will be assigned to c?
# c = 1



# 4. What will the following program display?
def main(): 
    x=1
    y = 3.4 
    print(x, y) # 1 3.4
    change_us(x, y)
    print(x, y) # 1 3.4

def change_us(a, b):
    a=0
    b=0 
    print(a, b) # 0 0

main()


# 5. Look at the following function definition:
def my_function(x, y): return x[y]

# a. Write a statement that calls this function 
# and uses keyword arguments to pass “testing” 
# into x and 2 into y.
print(my_function("testing", 2))

# b. What will be printed when the function 
# call executes? 
# s will be printed. it prints the subscript 
# 2 of the 'testing' array. which, is s.
# 


# 6. Write a statement that generates a random 
# number in the range of 1 through 100 and
# assigns it to a variable named rand.
import random
print(random.randrange(1, 101)) # up to but not including 101.


# 7. The following statement calls a function 
# named half, which returns a value that is 
# half that of the argument. (Assume the 
# number variable references a float value.) 
# Write code for the function.
def half(floatNum): return floatNum / 2

number = 10.0

result = half(number)

print(result)

# 8. A program contains the following 
# function definition:
def cube(num): return num * num * num
# Write a statement that passes the value 
# 4 to this function and assigns its 
# return value to the variable result.
result = cube(4)
print(result)


# 9. Write a function named times_ten that 
# accepts a number as an argument. When the 
# function is called, it should return the 
# value of its argument multiplied times 10.
def times_ten(number):
    return number * 10

print(times_ten(10))


# 10. Write a function named get_first_name 
# that asks the user to enter his or her 
# first name, and returns it.
def get_first_name():
    return print(input('enter your first name: '))

get_first_name()


