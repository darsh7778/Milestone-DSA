nums = [4,5,3,1,4,5,6,7,4,1]

# freq_map = {}

# for i in range(len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]] += 1
#     else:
#         freq_map[nums[i]] = 1

# print(freq_map)


# another aproach using hashmaps

hash_map = {}
n = len(nums)

for i in range(n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
    
print(hash_map[4])