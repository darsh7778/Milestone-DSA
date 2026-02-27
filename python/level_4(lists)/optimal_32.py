# optimal solution for finding the larget and second largest number in list 

l1 = [5, 10, 8]

largest = second = float("-inf")

for num in l1:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

print(f"largest is -> {largest},second largest is -> {second}")