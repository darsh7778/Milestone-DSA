def rotate_one_place(arr):
    n = len(arr)
    temp = arr[-1]
    
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
        
    arr[0] = temp

    return arr

arr = [1,2,3,4]
result = rotate_one_place(arr)

print(result)