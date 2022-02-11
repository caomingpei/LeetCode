from typing import *
from collections import defaultdict

nums = [9,4,1,7]
k = 2
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort(reverse=True)
        ans = float("inf")
        for i in range(len(nums)-k+1):
            print(nums[i],nums[i+k-1])
            ans = min(ans, nums[i]-nums[i+k-1])
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.minimumDifference(nums,k))