n = 1221

num = n
result = 0

while num > 0:
    last_digit = num % 10
    result = (result * 10)+ last_digit
    num = num // 10

if(result == n):
    print("palindrome")
else:
    print("not a palindrome")
    
