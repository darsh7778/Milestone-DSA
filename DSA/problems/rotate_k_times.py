def rotate_Array(arr, target):
    n = len(arr)
    temp = arr[n-target:]
    
    for i in range(n-target-1, -1, -1):
        arr[i+target] = arr[i]
        
    arr[:target] = temp
    return arr

arr = [1,2,3,4,5,6,7]
result = rotate_Array(arr, 3)
print(result)