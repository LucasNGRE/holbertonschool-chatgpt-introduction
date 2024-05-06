#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of an integer.

    Function Description:
        This recursive function calculates the factorial of a non-negative integer.

    Parameters:
        n (int): The non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of n.
    """
    if n == 0:  # If n is equal to 0
        return 1  # The factorial of 0 is 1
    else:
        return n * factorial(n-1)  # Otherwise, multiply n by the factorial of n-1

# Using the first command-line argument to calculate the factorial
f = factorial(int(sys.argv[1]))

# Printing the result
print(f)
