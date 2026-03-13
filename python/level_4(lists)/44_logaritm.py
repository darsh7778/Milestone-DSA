#count the number of digits using logarithm

from math import *

def count_digits(num):
    return int(log10(num)+1)

n = 6453
print(count_digits(n))