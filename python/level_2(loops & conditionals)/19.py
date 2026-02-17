#Print Fibonacci series up to N terms

num = int(input("write the number : "))

if(num<=0):
    print(f"enterd number {num} is not correct, It should be > 0.")

print(f"Fibonacci series of {num} is ->", end="" )
    
print(1, end=",")
if(num == 1):
    pass
else:
    print(1, end=",")
    prev = 1
    prev_prev = 1
    for n in range(3, num+1):
      print(prev+prev_prev, end=",")
      prev, prev_prev = prev + prev_prev, prev
    