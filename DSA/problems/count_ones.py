def count_ones(nums):
    n = len(nums)
    low, high = 0, n -1
    
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] >= 1:
            high = mid -1
        else:
            low = mid + 1
    return n - low
            
nums = [0,0,0,0,0,1,1,1,1]

ones = count_ones(nums)
print(ones)