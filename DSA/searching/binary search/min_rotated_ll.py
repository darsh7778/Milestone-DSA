# def find_min_two(nums):
#     low, high = 0, len(nums) - 1
#     mini = float('inf')
    
#     while low <= high:
#         mid = (low + high)//2
        
#         if nums[low] == nums[mid] == nums[high]:
#             low+=1
#             high-=1
#             continue
        
#         if nums[low] == nums[mid] or nums[mid] == nums[high]:
#             low +=1
#             continue
        
#         if nums[mid] <= nums[high]:
#             mini = min(mini, nums[mid])
#             high = mid - 1
#         else:
#             mini = min(mini, nums[low])
#             low = mid + 1
#     return mini

def find_min_two(nums):
    low, high = 0, len(nums) - 1
    mini = float('inf')
    
    while low <= high:
        mid = (low + high)//2
        
        # If already sorted
        if nums[low] <= nums[high]:
            mini = min(mini, nums[low])
            break
        
        # Handle duplicates (ONLY this)
        if nums[mid] == nums[high]:
            high -= 1
            continue
        
        # Right half sorted
        if nums[mid] < nums[high]:
            mini = min(mini, nums[mid])
            high = mid - 1
        else:
            mini = min(mini, nums[low])
            low = mid + 1
            
    return mini

nums = [2,2,2,2,0,2,2]
result = find_min_two(nums)
print(result)
        