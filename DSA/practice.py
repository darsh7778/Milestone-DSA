class Solution(object):
    def isPerfectSquare(self, num):
        if num < 0:
            return False

        low, high = 1, num 

        while low <= high:
            mid = (low+high)//2
            square = mid * mid

            if square == num:
                return True
            elif square > num:
                high = mid -1
            else:
                low = mid +1
        return False
    
num = int(input("num = "))
sol = Solution()
result = sol.isPerfectSquare(num)

print(result)

                



