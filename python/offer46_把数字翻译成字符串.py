from typing import *
num = 213215785914

class Solution:
    def translateNum(self, num: int) -> int:
        numstr = "0"+str(num)
        n = len(numstr)
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n):
            cur = int(numstr[i-1])*10 + int(numstr[i])
            if cur < 26 and cur>=10:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[n-1]



if __name__ == '__main__':
    res = Solution()
    print(res.translateNum(num))
