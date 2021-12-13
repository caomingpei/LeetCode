from typing import *
houses = [0,0,0,0,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = 5
n = 2
target = 3

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        houses = [c-1 for c in houses]
        INTMAX = 0x3f3f3f3f
        dp = [[[INTMAX for _ in range(target)] for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and houses[i] != j:
                    continue

                for k in range(target):
                    for j0 in range(n):
                        if j == j0:
                            if i == 0:
                                if k == 0:
                                    dp[i][j][k] = 0
                            else:
                                dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][k])
                        elif i >0 and k>0:
                            dp[i][j][k] = min(dp[i][j][k],dp[i-1][j0][k-1])

                    if dp[i][j][k] != INTMAX and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]

        ans = min(dp[m-1][j][target-1] for j in range(n))
        ans = -1 if ans == INTMAX else ans
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.minCost(houses, cost, m, n, target))