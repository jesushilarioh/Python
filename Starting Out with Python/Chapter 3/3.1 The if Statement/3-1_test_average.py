HIGH_SCORE = 95

test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 1: '))
test3 = int(input('Enter the score for test 1: '))

average = (test1 + test2 + test3) / 3

print('The average score is', average)

if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')