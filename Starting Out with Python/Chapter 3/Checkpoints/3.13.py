# 3.13 Convert the following code to an if-elif-else statement:
number = 4

if number == 1:
    print('One')
else:
    if number == 2:
        print('Two')
    else:
        if number == 3:
            print('Three')
        else:
            print('Unkown')
# ANSWER
if number == 1:
    print('One')
elif number == 2:
    print('Two')
elif number == 3:
    print('Three')
else:
    print('Unkown')