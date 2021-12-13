from typing import *
s = "ccaacabacb"

class Solution:
    INTMAX = 0x3f3f3f3f
    def predp(self,s,n):
        dp = [[True for i in range(n)] for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if dp[i+1][j-1] == True and s[i]==s[j]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp

    def minCut(self, s: str) -> int:
        n = len(s)
        dp = self.predp(s,n)
        if dp[0][n-1]:
            return 0
        cut = [self.INTMAX for i in range(n)]
        for i in range(0,n):
            if dp[0][i]:
                cut[i] = 0
            else:
                cut[i] = cut[i-1] + 1
                for j in range(0,i):
                    if dp[j+1][i]:
                        cut[i] = min(cut[i],cut[j]+1)

        return cut[n-1]

if __name__ == '__main__':
    res = Solution()
    print(res.minCut(s))
