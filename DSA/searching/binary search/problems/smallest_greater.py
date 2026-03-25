def smallestGreater(nums, target):
    low, high = 0, len(nums) -1
    
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] > target:
            high = mid -1
        else:
            low = mid +1
    
    if low == len(nums):
        return nums[0]
    else:
        return nums[low]

nums = ["a", "d", "f", "g", "k"]
result = smallestGreater(nums, "k")
print(result)

