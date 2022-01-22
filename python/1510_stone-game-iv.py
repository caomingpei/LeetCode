from typing import *
n = 4

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        dp[1] = True
        for i in range(2, n + 1):
            k = 1
            flag = False
            while k*k <= i:
                if dp[i-k*k] == False:
                    flag = True
                    break
                k += 1
            if flag:
                dp[i] = True
            else:
                dp[i] = False
        return dp[n]


if __name__ == '__main__':
    res = Solution()
    print(res.winnerSquareGame(n))