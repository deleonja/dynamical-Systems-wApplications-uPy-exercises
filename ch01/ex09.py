# Author: José Alfredo de León
# Date: 19.07.2020

# Book: Dynamical Systems with Applications using Python, 2018
# Exercise 1.9

# Carry out one hundred iterations on the recurrence relation
# x_{n+1} = 4x_n(1 − x_n),
# given that (a) x 0 = 0.2 and (b) x 0 = 0.2001. List the final ten
# iterates in each case.

# Create a recurrence function for the expression
def recurrence(x0, iterations):
    if (iterations == 1):
        return x0
    else:
        x = 4 * x0 * (1 - x0)
        return recurrence(x, iterations-1)

# Execute the x0 asked
print("x0 = 0.2, x100 = " + str(recurrence(0.2, 100)))
print("x0 = 0.2001, x100 = " + str(recurrence(0.2001, 100)))
