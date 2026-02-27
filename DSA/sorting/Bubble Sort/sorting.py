def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swap happened, array already sorted
            break


# Step 1: Ask size
n = int(input("Enter the size of array: "))

# Step 2: Create empty array
arr = []

# Step 3: Take elements one by one
for i in range(n):
    element = int(input(f"Enter array element {i+1}: "))
    arr.append(element)

# Step 4: Sort array
bubble_sort(arr)

print("sorted array =", arr)