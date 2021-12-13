from typing import *

nums = [2,3,-2,4,-5]

def threemax(a,b,c):
    return max(max(a,b),c)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        savmax = savmin = ans = nums[0]
        for i in range(1,len(nums)):
            b = savmax*nums[i]
            c = savmin*nums[i]
            savmax = threemax(nums[i], b, c)
            savmin = -threemax(-nums[i],-b,-c)
            ans = max(ans,savmax)

        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.maxProduct(nums))