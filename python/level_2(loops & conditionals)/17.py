#count the length of the string

str = input("enter the value - ")

print(len(str))

# count the length of a number 

num = int(input("enbter the number - "))
count = 0

while num > 0:
    num = num // 10
    count+=1
    
print("The total digit is :", count)

