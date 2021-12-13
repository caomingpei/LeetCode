from typing import *

nums = [5,1,6]

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INTMAX = 0x3f3f3f3f
        N = len(nums)
        if N < 3:
            return False
        small = float('inf')
        mid = float('inf')
        for i in range(N):
            if nums[i] < small:
                small = nums[i]
            elif nums[i] < mid and nums[i] > small:
                mid = nums[i]
            elif nums[i] > mid:
                return True
        return False

if __name__ == '__main__':
    res = Solution()
    print(res.increasingTriplet(nums))