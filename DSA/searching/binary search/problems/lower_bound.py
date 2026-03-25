def lower_bound(nums, target):
    n = len(nums)
    lb = n
    low, high = 0, n-1

    while low <= high:
        mid = (low + high)//2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb

# nums = [1, 1, 1, 2, 3, 3, 5, 6, 7, 7, 7, 9, 12, 12, 13]
nums = [3,4,5,6,7,7,8,9,9,9,10]
print(lower_bound(nums, 7))
        