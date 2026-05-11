def lower_bound(nums, target):
    n = len(nums)
    ub = -1
    low, high = 0, n-1

    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub - 1

nums = [1, 1, 1, 2, 3, 3, 5, 6, 7, 7, 7, 9, 12, 12, 13]
print(lower_bound(nums, 1))
        