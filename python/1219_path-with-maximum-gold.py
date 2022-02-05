from typing import *
grid = [[0,6,0],[5,8,7],[0,9,0]]

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        ans = 0
        ori=[[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(i,j,gold):
            cur = grid[i][j]
            grid[i][j] = 0
            gold += cur
            nonlocal ans
            ans = max(ans,gold)

            for x,y in ori:
                nx,ny = i+x,j+y
                if nx<0 or nx >=n or ny<0 or ny>=m or grid[nx][ny] == 0:
                    continue
                else:
                    dfs(nx,ny,gold)
            grid[i][j] = cur

        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]!=0:
                    dfs(i,j,0)

        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.getMaximumGold(grid))