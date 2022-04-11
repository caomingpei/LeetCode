from typing import *
n = 5

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        ans = 10
        choice = 9
        for i in range(n-1):
            choice *= 9-i
            ans += choice
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.countNumbersWithUniqueDigits(n))