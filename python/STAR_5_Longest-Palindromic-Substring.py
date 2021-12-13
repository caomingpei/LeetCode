from typing import *
s = "aaaaaa"


class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[True for i in range(n)] for i in range(n)]
        maxnum = 0
        ans = s[0]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                dp[i][j] = True if s[i] == s[j] and dp[i+1][j-1] else False
                if dp[i][j] and j-i> maxnum:
                    maxnum = j-i
                    ans = s[i:j+1]
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.longestPalindrome(s))