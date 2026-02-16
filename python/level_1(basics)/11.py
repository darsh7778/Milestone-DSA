#Check if a number is divisible by 5 and 11.

num = int(input("enter the number => "))

if(num % 5 == 0 and num % 11 == 0):
    print("YES, this number is divisible by 5 and 11 ")
else:
    print("NO, this number is not divisible by 5 and 11")