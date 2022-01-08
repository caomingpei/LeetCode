from typing import *

n = 2


class Solution:
    def grayCode(self, n: int) -> List[int]:
        maxm = 1<<n
        ans = [0 for _ in range(maxm)]
        for i in range(0,maxm):
            ans[i] = int(i/2)^i
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.grayCode(n))