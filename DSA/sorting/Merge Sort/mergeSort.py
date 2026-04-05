def merge_array(left,right):
    result = []
    i=j=0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    while i < len(left):
        result.append(left[i])
        i+=1
            
    while j < len(right):
        result.append(right[j])
        j+=1
            
    return result
            

def sort_array(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = sort_array(left_half)
    right_half = sort_array(right_half)
    
    return merge_array(left_half, right_half)

arr = [4,2,5,2,1,6,7,4]
result = sort_array(arr)
print(result)