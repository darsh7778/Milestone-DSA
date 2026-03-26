def missing(nums):
    n = len(nums)
    
    org_sum = n*(n+1)//2
    arr_sum = sum(nums)
    
    return org_sum - arr_sum

arr = [0,1,2,3]
result = missing(arr)
print(result)