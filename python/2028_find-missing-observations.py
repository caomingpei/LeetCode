from typing import *
from collections import deque

rolls = [1,5,6]
mean = 3
n = 4


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        misum = (n+m)*mean - sum(rolls)
        ans = [0 for _ in range(n)]
        if misum < n or misum > 6*n:
            return []
        eqdiv = misum // n
        maxcnt = misum - eqdiv * n
        for i in range(n):
            if i < maxcnt:
                ans[i] = eqdiv + 1
            else:
                ans[i] = eqdiv
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.missingRolls(rolls,mean,n))