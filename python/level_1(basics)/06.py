#Find the largest of three numbers

a = int(input("enter the number 1 = "))
b = int(input("enter the number 2 = "))
c = int(input("enter the number 3 = "))

if(a>b and a>c):
    print(a, "is largest")
elif(b>c):
    print(b, "is largest")
else:
    print(c, "is largest")