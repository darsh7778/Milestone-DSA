# find the gcd of two numbers by importing the package

import math

a = int(input("enter 1 number : "))
b = int(input("enter 2 number : "))

print("GCD is:", math.gcd(a, b))


# find the gcd of two numbers by logic

a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))

while b != 0:
    a, b = b, a%b
    
print("GCD is :", a)
