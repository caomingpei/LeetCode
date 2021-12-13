from typing import *

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        pre = [0] * (m+1)
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    pre[j] += 1
                else:
                    pre[j] = 0

            stack =[-1]
            for k in range(len(pre)):
                while stack and pre[stack[-1]] > pre[k]:
                    index = stack.pop()
                    ans = max(ans, pre[index]*(k-stack[-1]-1))
                stack.append(k)
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.maximalRectangle(matrix))