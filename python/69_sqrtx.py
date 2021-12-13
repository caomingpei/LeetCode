from typing import *

x = 0

class Solution:
    def bisect(self,tar):
        ans = -1
        l = 0
        r = tar + 1
        eps = 1e-6
        def check(mid,tar):
            if mid*mid - tar > eps:
                return True
            else:
                return False

        while(r - l > eps):
            mid = (l + r)/2
            if check(mid, tar):
                ans = mid
                r = mid
            else:
                l = mid
        return ans
    def mySqrt(self, x: int) -> int:
        num = self.bisect(x)
        return int(num)


if __name__ == '__main__':
    res = Solution()
    print(res.mySqrt(x))