def cycle_sort(arr):
    n = len(arr)
    
    for cycle_start in range(n - 1):
        item = arr[cycle_start]
    
        # Step 1: Find correct position
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
                            
        # If already in correct position
        if pos == cycle_start:
            continue
             
        # Step 2: Handle duplicates
        while item == arr[pos]:
            pos += 1
        
        # Step 3: Place item
        arr[pos], item = item, arr[pos]
        
        # Step 4: Rotate rest of cycle
        while pos != cycle_start:
            pos = cycle_start

            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1

            arr[pos], item = item, arr[pos]

    return arr

arr = [3,4,2,1,6]
result = cycle_sort(arr)
print(result)
