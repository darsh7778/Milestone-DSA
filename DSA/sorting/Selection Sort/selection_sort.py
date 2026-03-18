def selectionSort(arr):
    n = len(arr)
    mid_idx = 0
    
    for i in range(n):
        #assume current element is minimum
        mid_idx = i
        
        #find the smallest
        for j in range(i+1, n):
            if arr[j] < arr[mid_idx]:
                mid_idx = j
           
        #swap the smallest to the front
        arr[i], arr[mid_idx] = arr[mid_idx], arr[i]
    return arr
    

arr = [64, 25, 172, 22, 101]

sorted_arr = selectionSort(arr)
print("sorted array: ", sorted_arr) 