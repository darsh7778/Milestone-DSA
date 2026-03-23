def last_occurance(nums, target):
    n = len(nums)
    low, high = 0, n -1
    ub = n
    
    while low <= high:
        mid = (low+high)//2
        
        if nums[mid] > target:
            ub = mid
            high = mid -1
        else:
            low = mid +1
    return ub -1

nums = [1,2,3,4,4,4,5,6]
result = last_occurance(nums,4)
print(result)
    
            