def binary_search(arr, low, high, x):
    if low > high:
        return False
    
    mid = (low + high)//2
    
    if arr[mid] == x:
        return True
    elif arr[mid] < x:
        return binary_search(arr, mid+1, high, x)
    else:
        return binary_search(arr, low, mid-1, x)
    
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
    
result = binary_search(arr, 0, n-1, x)

if result:
    print("found")
else:
    print("not found")