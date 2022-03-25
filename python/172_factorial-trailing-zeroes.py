from typing import *

n = 100

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5,n+1,5):
            cur = i
            while cur % 5 == 0:
                cur /= 5
                ans += 1
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.trailingZeroes(n))