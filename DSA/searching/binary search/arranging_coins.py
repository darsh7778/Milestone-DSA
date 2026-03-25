def arrangeCoins(n):
    low, high = 0, n
    
    while low <= high:
        mid = (low + high)//2
        formula = mid * (mid + 1)//2
        
        if formula > n:
            high = mid - 1
        else:
            low = mid + 1
    return high

result = arrangeCoins(8)
print(result)