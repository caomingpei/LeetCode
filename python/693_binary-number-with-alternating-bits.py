from typing import *
from collections import deque

n = 7


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)
        return a & (a + 1) == 0


if __name__ == '__main__':
    res = Solution()
    print(res.hasAlternatingBits(n))