# Check if a number is palindrome

n = int(input("Enter a number"))
s = int(str(n)[::-1])

if(n==s):
    print("yes this is Palindrome ")
else:
    print("Not a Palindrome")
    
    
#Check if a number is palindrome without converting to the string

num = int(input("enter the number"))
original_num = num

reversed_num = 0

while 0 < num:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if(original_num == reversed_num):
    print("Palindrome")
else:
    print("Not a Palindrome")
    




