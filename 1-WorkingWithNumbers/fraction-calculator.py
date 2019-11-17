#!/usr/bin/env python3
"""
Write a calculator that can perform the basic mathematical operations on
two fractions. It should ask the user for two fractions and the operation the
user wants to carry out.
"""

from fractions import Fraction

if __name__ == '__main__':
    try:
        f1 = Fraction(input("Enter a valid fraction (a/b): "))
        f2 = Fraction(input("Enter another valid fraction (a/b): "))
    except ValueError:
        print("Invalid fraction specified")
        exit(1)

    operation = input("""Specify the operation on the fractions
        {ADD, SUBTRACT, MULTIPLY, DIVIDE}: """).upper()
    if operation == "ADD":
        print("The result of adding {0} and {1} is {2}".format(
            f1, f2, f1 + f2))
    elif operation == "SUBTRACT":
        print("The result of subtracting {1} from {0} is {2}".format(
            f1, f2, f1 - f2))
    elif operation == "MULTIPLY":
        print("The result of multiplying {0} and {1} is {2}".format(
            f1, f2, f1 * f2))
    elif operation == "DIVIDE":
        print("The result of dividing {0} by {1} is {2}".format(
            f1, f2, f1 / f2))
    else:
        print('Invalid Operation: ' + operation +
              '. Please choose one of: {ADD, SUBTRACT, MULTIPLY, DIVIDE}')
