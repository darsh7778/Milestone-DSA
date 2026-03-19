nums = [5,7,7,8,8,10]

def ciel_floor(nums, target):
    low, high = 0, len(nums) - 1
    floor, ciel = -1,-1
    
    while low <= high:
        mid = (low+high)//2
        
        if nums[mid] == target:
            return floor, ciel 
        elif nums[mid] > target:
            ciel = nums[mid]
            high = mid - 1
        else:
            floor = nums[mid]
            low = mid + 1
    return floor, ciel

result = ciel_floor(nums, 8)
print(result) 