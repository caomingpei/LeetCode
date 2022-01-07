from typing import *
from collections import deque

n = 9


class Solution:
    def lastRemaining(self, n: int) -> int:
        return 1 if n == 1 else 2 * (int(n / 2) + 1 - self.lastRemaining(int(n / 2)))


if __name__ == '__main__':
    res = Solution()
    print(res.lastRemaining(n))