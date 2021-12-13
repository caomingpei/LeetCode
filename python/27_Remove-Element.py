from typing import *
nums = [0,1,2,2,3,0,4,2]
val = 2

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        slowp, fastp = 0, 0
        while fastp < len(nums):
            if nums[fastp] == val:
                fastp += 1
            else:
                nums[slowp] = nums[fastp]
                slowp += 1
                fastp += 1
        return slowp

if __name__ == '__main__':
    res = Solution()
    print(res.removeElement(nums,val))