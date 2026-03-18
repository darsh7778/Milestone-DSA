# find the factors of a given number
n = 100

result = []
for i in range(1, (n//2)+1):
    if n % i == 0:
        result.append(i)
result.append(n)

print(result)

# optimal solution of a code 
