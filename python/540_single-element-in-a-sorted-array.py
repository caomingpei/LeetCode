from typing import *
from collections import defaultdict

nums = [1,1,3]
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] == nums[mid ^ 1]:
                l = mid + 1
            else:
                r = mid
        return nums[l]



if __name__ == '__main__':
    res = Solution()
    print(res.singleNonDuplicate(nums))