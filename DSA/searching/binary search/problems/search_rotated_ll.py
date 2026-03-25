def rotated_two(nums,target):
    n = len(nums)
    low, high = 0, n-1
    
    while low <= high:
        mid = (low+high)//2
        
        if nums[mid] == target:
            return True
        
        if nums[low] == nums[mid] == nums[high]:
            low +=1
            high -=1
            continue
        
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return False

nums = [7,7,7,7,1,2,3,7]
result = rotated_two(nums, 5)
print(result)
            