from typing import *
from collections import defaultdict


grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        ori = [(1,0),(-1,0),(0,1),(0,-1)]
        vis = [[False for _ in range(n)] for _ in range(m)]
        def dfs(x,y):
            if x<0 or x>=m or y<0 or y>=n or grid[x][y] == 0 or vis[x][y]:
                return
            vis[x][y] = True
            for ox, oy in ori:
                nx, ny = x + ox, y + oy
                dfs(nx, ny)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(1, n - 1):
            dfs(0, j)
            dfs(m - 1, j)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not vis[i][j] and grid[i][j]:
                    ans += 1
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.numEnclaves(grid))