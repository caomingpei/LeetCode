from typing import *
nums = [0,0,1,1,1,2,2,3,3,4]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slowp,fastp = 0,0
        while fastp < len(nums):
            if nums[slowp] == nums[fastp]:
                fastp += 1
            else:
                slowp += 1
                nums[slowp] = nums[fastp]
        return slowp+1
if __name__ == '__main__':
    res = Solution()
    print(res.removeDuplicates(nums))