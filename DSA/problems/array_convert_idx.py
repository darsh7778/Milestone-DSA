# Given an array with N distinct elements, convert the given array to a form where all elements are in the range of 0 to N-1

def idx_array(arr):
   sorted_arr = sorted(arr)

   rank = {}

   for i in range(n):
      rank[sorted_arr[i]] = i

   for num in arr:
      print(rank[num], end=" ")
    
    
n = int(input())

arr = list(map(int, input().split()))

idx_array(arr)
