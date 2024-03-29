# 6. Calories from Fat and Carbohydrates
# A nutritionist who works for a fitness club helps members by evaluating their diets. As part 
# of her evaluation, she asks members for the number of fat grams and carbohydrate grams 
# that they consumed in a day. Then, she calculates the number of calories that result from 
# the fat, using the following formula:

# calories from fat = fat grams x 9

# Next, she calculates the number of calories that result from the carbohydrates, using the 
# following formula:

# calories from carbs = carb grams x 4

# The nutritionist asks you to write a program that will make these calculations.


def main():
    number_of_fat_grams = float(input("Enter number of fat grams consumed in a day: "))
    number_of_carb_grams = float(input("Enter number of carb grams consumed in a day: "))

    calories_from_fat = calculate_calories_from_fat(number_of_fat_grams)
    calories_from_carbs = calculate_calories_from_carbs(number_of_carb_grams)

    print(f"Number of fat grams = {number_of_fat_grams:,.2f}")
    print(f"Number of Carbohydrate grams = {number_of_carb_grams:,.2f}")
    print(f"Calories from fat = {calories_from_fat:,.2f}")
    print(f"Calories from Carbohydrates = {calories_from_carbs:,.2f}")

def calculate_calories_from_fat(fat_grams):
    return fat_grams * 9

def calculate_calories_from_carbs(carb_grams):
    return carb_grams * 4

main()
