from typing import *
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans =[-1 for _ in range(n)]
        for j in range(n):
            col = j
            flag = 1
            for row in grid:
                cur = row[col]
                col += cur
                if col<0 or col>=n or row[col] != cur:
                    flag = 0
                    break
            if flag:
                ans[j] = col
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.findBall(grid))