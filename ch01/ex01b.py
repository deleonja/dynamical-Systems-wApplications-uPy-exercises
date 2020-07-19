# 1.b. Write a Python program that sums the subset of prime numbers
# up to some natural number, n, say.

import sys
import numpy as np
import math


def is_prime(number):
    if number % 2 == 0 and number > 2:
        return False
    print(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))
    return all(number % i for i in range(3, math.ceil(number), 2))


print(is_prime(13))

n = int(sys.argv[1])
list = np.arange(1, n+1)
foo = np.vectorize(is_prime)
pbools = foo(list)
primes = np.extract(pbools, list)

sum = 0
for prime in primes:
    sum = sum + prime

print("Sum = " + str(sum))
