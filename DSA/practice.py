def maxProfit(nums):
    n = len(nums)
    maxi = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                p = nums[j] - nums[i]
                maxi = max(maxi, p)
            
    return maxi

nums = [6,4,3,1]
result = maxProfit(nums)
print(result)
            
        
            