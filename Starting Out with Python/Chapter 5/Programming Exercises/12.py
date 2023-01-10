# 12. Maximum of Two Values
# Write a function named max that accepts 
# two integer values as arguments and returns 
# the value that is the greater of the two. For 
# example, if 7 and 12 are passed as arguments to 
# the function, the function should return 12. 
# Use the function in a program that prompts the 
# user to enter two integer values. The program 
# should display the value that is the greater 
# of the two.

def main():
    num1, num2 = getTwoIntegers()
    greater_value = max(num1, num2)
    print(f"greater value = {greater_value}")

def max(num1, num2):
    if num1 >= num2:
        return num1
    if num2 >= num1:
        return num2
    return num1

def getTwoIntegers():
    num1 = input("Enter 1st number: ")
    num2 = input("Enter 2nd number: ")
    return num1, num2
    
main()