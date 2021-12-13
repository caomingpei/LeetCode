from typing import *
steps = 2
arrLen = 4

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = int(1e9 + 7)
        minNum = min(steps + 1, arrLen)
        dp = [[0 for _ in range(minNum + 1)] for _ in range(steps + 1)]
        dp [0][0] = 1

        for i in range(1,steps + 1):
            for j in range(0,minNum):
                dp[i][j] = dp[i-1][j]
                if j >= 1:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
                if j < minNum:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % MOD

        return dp[steps][0]

if __name__ == '__main__':
    res = Solution()
    print(res.numWays(steps,arrLen))