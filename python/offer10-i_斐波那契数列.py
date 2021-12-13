from typing import *
n = 5

class Solution:
    def fib(self, n: int) -> int:
        MOD = 1e9+7
        if n == 0: return 0
        if n == 1: return 1

        def cals(i, f0, f1):
            if i == n:
                return (f0 + f1) % MOD
            fth = (f0 + f1) % MOD
            return cals(i+1, f1, fth)

        return int(cals(2, 0, 1))


if __name__ == '__main__':
    res = Solution()
    print(res.fib(n))
