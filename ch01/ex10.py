# Author: José Alfredo de León
# Date: 19.07.2020

# Book: Dynamical Systems with Applications using Python, 2018
# Exercise 1.10

import sys

# Check that command line in terminal is ok
if (len(sys.argv) == 1):
    print("Two numbers were expected after execution command.")
    sys.exit()
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

# Construct a function with Euclid algorithm
def Euclid(num1, num2):
    while (num1 % num2):
        dummy = num1 % num2
        num1 = num2
        num2 = dummy
    return num1

# Find mcd taking into account that one doesn't know apriori if a>b
if (a > b):
    mcd = Euclid(a, b)
else:
    c = a
    a = b
    b = c
    mcd = Euclid(a, b)

print("mcd between " + str(a) + " and " + str(b) + " is " + str(mcd))
