#leetcode problem no. 34
class Solution:
    def lower_bound(self, nums, target):
        n = len(nums)
        lb = n
        low, high = 0, n-1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
    
    def upper_bound(self, nums, target):
        n = len(nums)
        ub = n
        low, high = 0, n-1

        while low <= high:
            mid = (low + high)//2
        
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1

        return ub
    
    def search_occurances(self, nums, target):
        lb = self.lower_bound(nums, target)
        ub = self.upper_bound(nums, target)
        
        if lb == len(nums) or target != nums[lb]:
            return -1,-1
        
        return lb, ub-1

sol = Solution()

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

result = sol.search_occurances(nums, target)
print(result)
        
        
        
