# 1. Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, then converts that 
# distance to miles. The conversion formula is as follows:
# Miles = Kilometers x 0.6214

def kilometers_to_miles(number):
    return number * 0.6214

def main():
    distance_in_kiometers = float(input('Enter distance in kilometers: ')) 
    distance_in_miles = kilometers_to_miles(distance_in_kiometers)
    print(f"Kilometers = {distance_in_kiometers}\nMiles = {distance_in_miles}")

main()