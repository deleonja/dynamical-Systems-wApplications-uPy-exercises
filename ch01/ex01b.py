# Author: José Alfredo de León
# Date: 18.07.2020

# Book: Dynamical Systems with Applications using Python, 2018
# Exercise 1.b

# Write a Python program that sums the subset of prime numbers
# up to some natural number, n, say.

import sys
import numpy as np
import math


def is_prime(number):
    '''
    Function to check whether a number is prime or not.

    Example:
    is_prime(2) = True
    is_prime(6) = False
    '''
    # Check if number is divisible by 2 and greater then two
    if number % 2 == 0 and number > 2:
        return False
    return all(number % i for i in range(3, math.ceil(number), 2))


# Take number n from command line inserted in terminal
n = int(sys.argv[1])

# Find prime numbers in [1,n]
list = np.arange(1, n+1)
foo = np.vectorize(is_prime)
pbools = foo(list)
primes = np.extract(pbools, list)

# Sum all the primes
sum = 0
for prime in primes:
    sum = sum + prime

# Print the sum
print("Sum = " + str(sum))
