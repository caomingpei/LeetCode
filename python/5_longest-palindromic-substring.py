from typing import *
s = "babad"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [ [True for _ in range(n)] for _ in range(n)]
        ans = s[0]
        maxnum = 0
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else False
                if dp[i][j] and j-i > maxnum:
                    maxnum = j-i
                    ans = s[i:j+1]
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.longestPalindrome(s))