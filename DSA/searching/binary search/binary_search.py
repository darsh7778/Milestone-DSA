def search(nums, target):
    #initialize 
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        # calculate mid 
        mid = (low+high)//2
        
        if nums[mid] == target: #compare
            return mid
        elif nums[mid] < target:
            low = mid+1
        else:
            high = mid - 1
    return -1

arr = [1,3,4,5,11,13,15,19,21]
result = search(arr, 3)
print(result)
        
    