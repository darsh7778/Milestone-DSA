def search(nums, target):
    n = len(nums)
    low, high = 0, n-1

    while low <= high:
        mid = (low + high)//2

        if nums[mid] == target:
            return mid

        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid +1 
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid -1
            else:
                low = mid + 1
    return -1

nums = [17,18,19,20,1,2,2,3,4,5,6,7,8,9]
result = search(nums, 2)

print(result)