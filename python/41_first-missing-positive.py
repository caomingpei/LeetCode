from typing import *
nums = [3,4,-1,1]

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        LENMAX = int(5e5+1)
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = LENMAX

        for i in range(len(nums)):
            num = abs(nums[i])
            if num < LENMAX:
                nums[num-1] = -abs(nums[num-1])

        ans = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans = i+1
                break
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.firstMissingPositive(nums))