def mismatch(arr):
    nums = sorted(arr)
    
    for num in nums:
        if num+1 != nums[+1]:
            return num, num+1
    
    return -1

arr = [1,2,2,4]
res = mismatch(arr)
print(res)