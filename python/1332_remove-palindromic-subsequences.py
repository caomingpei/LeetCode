from typing import *
s = "ababa"

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        i = 0
        j = n-1
        while i <= j:
            if s[i] != s[j]:
                return 2
            i += 1
            j -= 1
        return 1

if __name__ == '__main__':
    res = Solution()
    print(res.removePalindromeSub(s))