from typing import *
from collections import deque
isWater = [[0,0,1],[1,0,0],[0,0,0]]

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        ori = [[0,1],[0,-1],[-1,0],[1,0]]

        def check(x, y):
            if x < 0 or y < 0 or x >= n or y >= m or mat[x][y] != -1:
                return False
            return True

        mat = [[-1 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    mat[i][j] = 0
                    q.append((i, j, 0))
        while q:
            curx, cury, depth = q.popleft()
            for x, y in ori:
                nx, ny = curx + x, cury + y
                if check(nx, ny):
                    mat[nx][ny] = depth + 1
                    q.append((nx, ny, depth + 1))

        return mat


if __name__ == '__main__':
    res = Solution()
    print(res.highestPeak(isWater))

