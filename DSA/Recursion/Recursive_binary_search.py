def binarySearch(arr, left, right, target):
    if left > right:
        return -1
    
    mid = (left+right)//2
    
    if arr[mid] == target:
        return mid
    
    if arr[mid] > target:
        return binarySearch(arr, left, mid-1, target)
    else:
        return binarySearch(arr, mid+1, right, target)
    
arr = [2,3,4,6,9,10]
target = 9
result = binarySearch(arr, 0, len(arr)-1, target)

print(result)
        
