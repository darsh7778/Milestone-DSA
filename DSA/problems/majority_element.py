# Given an array nums of size n, return the majority element.

def majority_element(num):
    count = 0
    candidate = None
    
    for nums in num:
        if count == 0:
            candidate = nums
        
        if nums == candidate:
            count += 1
            print(count)
        else:
            count -= 1
            print(count)
            
    return candidate # agar niche wali step use kar rahe he to ise skip karna

    # verification step 
    # this step is optional because problem me clearly bola gaya hai 👇
    # The majority element always exists in the array. Matlab-> majority element > n/2
    
    # for nums in num:
    #     if nums == candidate:
    #         count += 1
    
    # if count > len(num) // 2:
    #     return candidate
    # else:
    #     return -1
        

num = [4,5,2,2,1,6]
result = majority_element(num)

print(result)