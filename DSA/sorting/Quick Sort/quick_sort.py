def partition(nums, low, high):
    pivot = nums[low]
    i,j = low, high
    
    while i < j:
        while nums[i] <= pivot and i <= high-1:
            i+=1
        
        while nums[j] > pivot and j >= low+1:
            j-=1
        
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
            
    nums[low], nums[j] = nums[j], nums[low]  
    return j

def quick_sort(nums, low, high):
    if low < high:
        p_ind = partition(nums, low, high)
        quick_sort(nums, low, p_ind -1)
        quick_sort(nums, p_ind+1, high)
        
arr = [3,4,2,1,5,3,2]
n = len(arr)

quick_sort(arr, 0, n-1)
print(arr)
