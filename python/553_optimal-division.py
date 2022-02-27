from typing import *
nums = [1000,100,10,2]

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        elif n == 2:
            return str(nums[0])+"/"+str(nums[1])
        else:
            ans = ""
            ans += str(nums[0]) + "/("
            for i in range(1,n-1):
                ans += str(nums[i])
                ans += "/"
            ans += str(nums[-1])+")"
            return ans

if __name__ == '__main__':
    res = Solution()
    print(res.optimalDivision(nums))