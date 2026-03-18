def pushZeros(arr):
    n = len(arr)
    j = 0
    
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

arr = [4,3,0,0,2,0,1]
result = pushZeros(arr)
print(result)
        
            