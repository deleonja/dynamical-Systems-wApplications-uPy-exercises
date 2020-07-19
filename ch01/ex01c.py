# Author: José Alfredo de León
# Date: 19.07.2020

# Book: Dynamical Systems with Applications using Python, 2018
# Exercise 1.c:

# Consider Pythagorean triples, positive integers a, b, c, such that
# a^2 + b^2 = c^2. Suppose that c is defined by c = b + n, where n is
# also an integer. Write a Python program that will find all such
# triples for a given value of n, where both a and b are less than or
# equal to a maximum value, m, say. For the case n = 1, find all
# triples with 1 ≤ a ≤ 100 and 1 ≤ b ≤ 100. For the case n = 3,
# find all triples with 1 ≤ a ≤ 200 and 1 ≤ b ≤ 200.

# Import numpy to avoid looping
import numpy as np

# Create a function that solves the exercise for any value of n and m
def PythagoreanTriples(n, m):
    '''
    Function to find Pythagorean triples (a, b, c) for any integer in
    [1,m] satisfying:
    > a^2 + b^2 = c^2
    > c = b + n.

    Example:
    PythagoreanTriples(2,2) = np.array([[2.82843, 1, 3],
                                        [3.46410, 2, 4]])
    '''
    # Create an array with all posible values of b
    b = np.arange(1, m + 1)
    # Create an array of size m with n in all entries
    n_array = np.array([n]*m)
    # Calculate all possible values of a
    a = np.sqrt(2*n*b + n_array**2)

    # Arrange triples in an array
    triples = np.array([a, b, b + n])
    triples = np.transpose(triples)

    # Return array with triples
    return triples

firstCase = PythagoreanTriples(1, 100)
secondCase = PythagoreanTriples(3, 200)

print(firstCase)
print("\n\n\n")
print(secondCase)
