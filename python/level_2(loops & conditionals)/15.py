#Reverse a number

num = int(input("enter the number = "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
    
print("the reversed number is", reversed_num)
    


#Reverse a number by using string slicing

n = int(input("enter the number = "))

reversed_number = int(str(n)[::-1])
    
print("reversed number =>", reversed_number)