def peak_ele(nums):
    low, high = 0, len(nums) -1
    
    while low < high:
        mid = (low + high)//2
        
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid 
    return low
        
def find_peak(nums):
    n = len(nums)
    low, high = 0, n -1
    
    while low <= high:
        mid = (low+high)//2
        
        if ((mid == 0) or nums[mid-1] < nums[mid]) and ((mid == n-1) or nums[mid+1] < nums[mid]):
            return mid
        
        elif mid > 0 and nums[mid -1] > nums[mid]:
            high = mid -1
        else:
            low = mid+1
    return -1
    
nums= [1,2,3,2,1]
result = find_peak(nums)
print(result)

