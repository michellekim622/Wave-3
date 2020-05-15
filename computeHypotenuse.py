# Compute the Hypotenuse
from math import sqrt

def pythagorean(a, b):
    return sqrt(a**2 + b**2)

print("Input lengths of shorter triangle sides:")
a = float(input("a:"))
b = float(input("b:"))

print("The length of the hypotenuse is :", pythagorean(a, b))
