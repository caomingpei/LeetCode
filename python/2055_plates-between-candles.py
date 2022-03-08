from typing import *

s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        preSum = [0 for _ in range(n)]
        sum = 0
        left = [0 for _ in range(n)]
        lind = -1
        for i in range(n):
            if s[i] == "*":
                sum += 1
            else:
                lind = i
            preSum[i] = sum
            left[i] = lind

        right = [0 for _ in range(n)]
        rind = -1
        for i in range(n-1,-1,-1):
            if s[i]=="|":
                rind = i
            right[i] = rind

        ans = [0 for _ in range(len(queries))]
        for i, (x,y) in enumerate(queries):
            l,r = right[x], left[y]
            if l >= 0 and r >= 0 and l < r:
                ans[i] = preSum[r] - preSum[l]

        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.platesBetweenCandles(s,queries))