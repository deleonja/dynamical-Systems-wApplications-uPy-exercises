# Author: José Alfredo de León
# Date: 18.07.2020

# Book: Dynamical Systems with Applications using Python, 2018
# Exercise 1.b:
# Write a Python program that sums the subset of prime numbers
# up to some natural number, n, say.

# The code to get the list of prime numbers in [2,n] was taken and
# modified from
# https://stackoverflow.com/questions/36095518/get-prime-numbers-from-numpy-array/36095942

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
    # Return True if number is divisible by 2 and greater then two
    if number % 2 == 0 and number > 2:
        return False

    # Return True if number is divisible by all integers [3,n**(1/2)]
    return all(number % i for i in range(3, math.ceil(number), 2))


# Take number n from command line inserted in terminal
if len(sys.argv) == 1:
    print("Number n was expected after execution instruction. Like this:")
    print("'python3 ex01b.py n'")
    sys.exit()
else:
    n = int(sys.argv[1])

# Find prime numbers in [1,n]
list = np.arange(1, n + 1)
foo = np.vectorize(is_prime)
pbools = foo(list)
primes = np.extract(pbools, list)

# Sum all the primes
primeSum = np.sum(primes)

# Print the sum
print("Sum = " + str(primeSum))
