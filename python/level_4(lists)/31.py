# find the largest element in list 

l1 = [2, 1, 5, 6, 9, -29, -2423]

largest = l1[0]

for num in l1:
    if num > largest:
        largest = num
        
print("using loop",largest)
        

# using max method

large = max(l1)

print("using the max method", large)
