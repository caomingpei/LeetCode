from typing import *
n = 10

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        num = n // 3
        if n % 3 == 0:
            return pow(3, num)
        elif n % 3 == 1:
            return pow(3, num-1) * 4
        else:
            return pow(3, num) * 2


if __name__ == '__main__':
    res = Solution()
    print(res.integerBreak(n))