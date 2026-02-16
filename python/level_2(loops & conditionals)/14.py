#Find factorial of a number

n = int(input("enter the number => "))

fact = 1

if (n == 1 or n == 0):
    print(1)
else:
    for i in range(1, n+1):
        fact*=i

print(f"the factorial of {n} is {fact}")    