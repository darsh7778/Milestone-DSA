def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(bubble_sort_optimized([1, 2, 3, 4]))      # already sorted
print(bubble_sort_optimized([4, 3, 2, 1]))      # reverse sorted
print(bubble_sort_optimized([5, 1, 4, 2, 8]))   # random
print(bubble_sort_optimized([1]))               # single element
print(bubble_sort_optimized([]))                # empty list