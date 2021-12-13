from typing import *

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        INTINF = 0x3f3f3f3f
        n = len(triangle)
        sav = [INTINF for _ in range(n)]
        sav [0] = 0
        for i in range(n):
            for j in range(i,0,-1):
                sav[j] = min(sav[j-1], sav[j]) + triangle[i][j]
            sav[0] += triangle[i][0]
        ans = INTINF
        for i in range(n):
            ans = min(ans, sav[i])
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.minimumTotal(triangle))