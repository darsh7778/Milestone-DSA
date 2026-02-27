# Find second largest element 

l1 = [34, 43, 23, 93, 90, -2342, -324, 123, 43345, 40033, 45555]
n = len(l1)

largest = float("-inf")
s_largest = float("-inf")

for i in range(0, n):
    largest = max(l1[i], largest)
        
print("Largest :",largest)

for i in range(0, n):
    if l1[i] > s_largest and l1[i] != largest:
        s_largest = l1[i]
        
print("second largest", s_largest)
    
    
        
