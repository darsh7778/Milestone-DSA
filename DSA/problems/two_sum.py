def two_sum(nums, target):
    n = len(nums)
    hash_map = {}
    
    for i in range(0,n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        else:
            hash_map[nums[i]] = i

arr = [2,3,4,5,7]
result = two_sum(arr, 10)
print(result)
            