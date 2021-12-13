from typing import *

nums = [3,4,2]

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxVal = int(1e4 + 1)
        bucket = [0 for _ in range(maxVal)]
        for num in nums:
            bucket[num] += num

        size = len(bucket)
        dp = [0 for _ in range(maxVal)]
        dp[0] = bucket[0]
        dp[1] = max(bucket[0], bucket[1])
        for i in range(2, size):
            dp[i] = max(dp[i-1], dp[i-2] + bucket[i])

        return dp[size-1]

if __name__ == '__main__':
    res = Solution()
    print(res.deleteAndEarn(nums))