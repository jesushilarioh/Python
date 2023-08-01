# 5. Test Average and Grade
# Write a program that asks the user to 
# enter five test scores. The program should 
# display a letter grade for each score and 
# the average test score. Write the following 
# functions in the program:

# • calc_average. This function should accept 
# five test scores as arguments and return the 
# average of the scores.

# • determine_grade. This function should 
# accept a test score as an argument and return 
# a letter grade for the score based on the 
# following grading scale:

# Score         Letter Grade
#-------------------------------
# 90-100            A
# 80-89             B
# 70-79             C
# 60-69             D
# Below 60          F
#

def getTestScore(prompt):
    testScore = float(input(prompt))

    while (testScore < 0):
        testScore = float(input("enter a score 0 or greater: "))

    return testScore

def calc_average(score1, score2, score3, score4, score5):
    return (score1 + score2 + score3 + score4 + score5) / 5

def determine_grade(test_score):
    if (test_score <= 100 and test_score >= 90):return 'A'
    if (test_score <= 89 and test_score >= 80): return 'B'
    if (test_score <= 79 and test_score >= 70): return 'C'
    if (test_score <= 69 and test_score >= 60): return 'D'
    if (test_score < 60): return 'F'
    
def main():
    test_score_1 = getTestScore("Enter score #1: ")
    test_score_2 = getTestScore("Enter score #2: ")
    test_score_3 = getTestScore("Enter score #3: ")
    test_score_4 = getTestScore("Enter score #4: ")
    test_score_5 = getTestScore("Enter score #5: ")

    test_score_1_grade_letter = determine_grade(test_score_1)
    test_score_2_grade_letter = determine_grade(test_score_2)
    test_score_3_grade_letter = determine_grade(test_score_3)
    test_score_4_grade_letter = determine_grade(test_score_4)
    test_score_5_grade_letter = determine_grade(test_score_5)

    test_score_average = calc_average(test_score_1, test_score_2, test_score_3, test_score_4, test_score_5)

    print("Score\tLetter Grade") 
    print("-------------------------")  
    print(f"1. {test_score_1}  {test_score_1_grade_letter}") 
    print(f"2. {test_score_2}  {test_score_2_grade_letter}") 
    print(f"3. {test_score_3}  {test_score_3_grade_letter}") 
    print(f"4. {test_score_4}  {test_score_4_grade_letter}") 
    print(f"5. {test_score_5}  {test_score_5_grade_letter}") 
    print("-------------------------")
    print(f"Average grade: {test_score_average}")
    print(f"Average Letter Grade: {determine_grade(test_score_average)}")
     

main()