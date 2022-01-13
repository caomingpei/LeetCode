from typing import *
from collections import deque
nums = [0,0,3,2]

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        mindex = 0
        mmax = 0
        smax = 0
        for i in range(len(nums)):
            if nums[i] > smax and nums[i] < mmax:
                smax = nums[i]
            elif nums[i] > mmax:
                smax = mmax
                mmax = nums[i]
                mindex = i

        if mmax >= 2*smax:
            return mindex
        return -1


if __name__ == '__main__':
    res = Solution()
    print(res.dominantIndex(nums))

