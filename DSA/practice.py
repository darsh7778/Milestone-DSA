def func(n):
    if n == 2:
        return 2
    
    return n * func(n-1)

print(func(4))