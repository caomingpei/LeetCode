from typing import *

n = 3

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        t = 0
        b = n-1
        l = 0
        r = n-1
        ind = 1
        while True:
            for i in range(l,r + 1):
                ans[t][i] = ind
                ind += 1
            t += 1
            for i in range(t,b + 1):
                ans[i][r] = ind
                ind += 1
            r -= 1
            for i in range(r,l-1,-1):
                ans[b][i] = ind
                ind += 1
            b -= 1
            for i in range(b,t-1,-1):
                ans[i][l] = ind
                ind += 1
            l += 1
            if r < l:
                break
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.generateMatrix(n))