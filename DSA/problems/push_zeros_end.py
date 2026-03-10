# push zeros to end while maintaining the relative order of other elements
# def push_zero_end(arr):
#     count = 0
#     n = len(arr)
    
#     for i in range(n):
#         if arr[i] != 0:
#             arr[count] = arr[i]
#             count+=1
    
#     while (count < n):
#         arr[count] = 0
#         count+=1



# optimal solution      
# def push_zero_end(arr):
#     n = len(arr)
#     j = 0

#     for i in range(n):
#         if arr[i] != 0:
#             arr[i], arr[j] = arr[j], arr[i]
#             j += 1
 
 
            
# arr = [1,0,3,0,5,4,6,0,1,2,4]
# push_zero_end(arr)
# print(arr)
        