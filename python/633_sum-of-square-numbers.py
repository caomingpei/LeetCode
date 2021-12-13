import math
from typing import *
c = 5

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b =int(math.sqrt(c))+1
        while a<=b:
            if a**2 + b**2 == c:
                return True
            elif a**2 + b**2 < c:
                a += 1
            else:
                b -= 1
        return False

if __name__ == '__main__':
    res = Solution()
    print(res.judgeSquareSum(c))