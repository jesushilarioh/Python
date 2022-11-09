# 2. String Repeater
# Python allows you to repeat a string by multiplying it by an integer, for example, 'Hi' * 3
# will give 'HiHiHi'. Pretend that this feature does not exist, and instead write a function 
# named repeat that accepts a string and an integer as arguments. The function should 
# return a string of the original string repeated the specified number of times, for example, 
# repeat('Hi', 3) should return 'HiHiHi'

def repeat(string, number):
    return string * number
    
def main():
    print(repeat("Hi", 5))

main()