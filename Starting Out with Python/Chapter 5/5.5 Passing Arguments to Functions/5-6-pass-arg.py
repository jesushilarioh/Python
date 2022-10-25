# This program demonstrates an argument being
# passed to a function.

from typing import MappingView


def main():
    value = 3000
    show_double(value)

def show_double(number):
    result = number * 2
    print(result)

main()
