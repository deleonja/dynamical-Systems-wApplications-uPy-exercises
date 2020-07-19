# Author: José Alfredo de León
# Date: 18.07.2020

# Book: Dynamical Systems with Applications using Python, 2018
# Exercise 1.a

# Write a function for converting degrees Fahrenheit to degrees
# Centigrade.

def FtoC(F):
    '''
    Function to convert degrees Fahrenheit to degrees Centigrade.

    Example:
    FtoC(50) = 5/9*(50-32) =
    '''
    Centigrade = 5/9*(F - 32)
    return Centigrade
