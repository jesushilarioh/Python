
# 14. Kinetic Energy

# In physics, an object that is in motion 
# is said to have kinetic energy. The following formula 
# can be used to determine a moving object’s 
# kinetic energy:

# KE = 1/2 mv^2

# The variables in the formula are as follows: 
# KE is the kinetic energy, m is the object’s mass 
# in kilograms, and v is the object’s velocity in
# meters per second.
# Write a function named kinetic_energy that 
# accepts an object’s mass (in kilograms) 
# and velocity (in meters per second) as arguments. 
# The function should return the amount 
# of kinetic energy that the object has. Write a 
# program that asks the user to enter values 
# for mass and velocity, then calls the 
# kinetic_energy function to get the object’s 
# kinetic energy.

# 3. Write a program that asks the user to enter 
# values for mass and velocity, then calls the 
# kinetic_energy function to get the object’s 
# kinetic energy.
def main():
    mass = getFloat("Enter value for mass: ")
    velocity = getFloat("Enter value for velocity: ")

    print(f"the kinetic_energy is {kinetic_energy(mass, velocity)}")

def getFloat(prompt):
    user_input = float(input(prompt))

    while(user_input <= 0):
        user_input = float(input("Enter number greater than 0: "))

    return user_input

def kinetic_energy(mass, velocity):
    return (1 / 2) * (mass * (pow(velocity, 2)))

main()
