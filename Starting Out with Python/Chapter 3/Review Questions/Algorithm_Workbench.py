# 1. Write an if statement that assigns 20 to the variable y, 
#   and assigns 40 to the variable z if the variable x is greater 
#   than 100.
x = 101.0
if x > 100:
    y = 20
    z = 40

# 2. Write an if statement that assigns 10 to the variable b, and 
#   50 to the variable c if the variable a is equal to 100.
a = 100
if a == 100:
    b = 10
    c = 50

# 3. Write an if-else statement that assigns 0 to the variable b 
#   if the variable a is less than 10. Otherwise, it should 
#   assign 99 to the variable b.
a = 9
if a < 10:
    b = 0
else:
    b = 99

# 4. The following code contains several nested if-else statements. 
#   Unfortunately, it was written without proper alignment and 
#   indentation. Rewrite the code and use the proper conventions 
#   of alignment and indentation.

# if score >= A_score: 
#     print('Your grade is A.') 
# else:
# if score >= B_score: 
#     print('Your grade is B.') 
# else:
# if score >= C_score: 
#     print('Your grade is C.') 
# else:
# if score >= D_score: 
#     print('Your grade is D.') 
# else:
#     print('Your grade is F.')
A_score = 90
B_score = 80
C_score = 70
D_score = 60

score = 99

if score >= A_score: 
    print('Your grade is A.') 
else:
    if score >= B_score: 
        print('Your grade is B.') 
    else:
        if score >= C_score: 
            print('Your grade is C.') 
        else:
            if score >= D_score: 
                print('Your grade is D.') 
            else:
                print('Your grade is F.')


# 5. Write nested decision structures that perform the following: 
#   If amount1 is greater than 10 and amount2 is less than 100, 
#   display the greater of amount1 and amount2.
amount1 = 25
amount2 = 90
if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print('amount1 =', amount1)
        else:
            print('amount2 =', amount2)

# 6. Write an if-else statement that assigns True to the again variable 
#   if the score variable is within the range of 40 to 49. If the 
#   score variable’s value is outside this range, assign False to 
#   the again variable.
score = 47

if score >= 40 and score <= 49:
    again = True
else:
    again = False

print(again)

# 7. Write an if-else statement that determines whether the 
#   points variable is outside the range of 9 to 51. If 
#   the variable’s value is outside this range it should 
#   display “Invalid points.” Otherwise, it should display 
#   “Valid points.”
points = 10.2

if points < 9 or points > 51:
    print('"Invalid points"')
else:
    print('"Valid points"')

# 8. Write an if statement that uses the turtle graphics 
#   library to determine whether the turtle’s heading is 
#   in the range of 0 degrees to 45 degrees (including 0 
#   and 45 in the range). If so, raise the turtle’s pen.

# 9. Write an if statement that uses the turtle graphics 
#   library to determine whether the turtle’s pen size is 
#   greater than 1 or the pen color is red. If so, set the 
#   pen size to 1 and the pen color to blue.

# 10. Write an if statement that uses the turtle graphics 
#   library to determine whether the turtle is inside of a 
#   rectangle. The rectangle’s upper-left corner is at 
#   (100, 100) and its lower-right corner is at (200, 200). 
#   If the turtle is inside the rectangle, hide the turtle.