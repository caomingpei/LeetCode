from typing import *
from collections import defaultdict

nums = [1,2,2,1]
k = 1
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        for num in nums:
            ans = ans + cnt[num-k] + cnt[num+k]
            cnt[num] += 1
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.countKDifference(nums,k))