from typing import *
nums = [4,2,0,2,3,2,0]
from bisect import bisect_right

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = len(nums)-1
        while pos and nums[pos] <= nums[pos-1]:
            pos -= 1
        l = nums[pos:]
        l.reverse()
        nums[pos:] = l
        if pos>0:
            ind = bisect_right(nums,nums[pos-1],pos,len(nums))
            nums[pos-1],nums[ind] = nums[ind], nums[pos-1]

if __name__ == '__main__':
    res = Solution()
    print(res.nextPermutation(nums))
    print(nums)