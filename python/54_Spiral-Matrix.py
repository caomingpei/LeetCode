from typing import *

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n = len(matrix)
        m = len(matrix[0])
        vis = [[False for _ in range(m)] for _ in range(n)]
        ans = []

        def check(nextx,nexty):
            if nextx < 0 or nexty <0 or nextx >= n or nexty >=m:
                return False
            if vis[nextx][nexty]:
                return False
            return True

        def dfs(curx,cury,d):
            vis[curx][cury] = True
            ans.append(matrix[curx][cury])
            if check(curx + d[0],cury + d[1]):
                dfs(curx + d[0],cury + d[1], d)
            else:
                for d in dir:
                    nextx = curx + d[0]
                    nexty = cury + d[1]
                    if check(nextx,nexty):
                        dfs(nextx,nexty,d)

        dfs(0,0,(0, 1))
        return ans

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t = 0
        d = len(matrix) -1
        l = 0
        r = len(matrix[0]) -1
        ans = []
        while True:
            for i in range(l, r + 1):
                ans.append(matrix[t][i])
            t += 1
            if t > d:
                break
            for i in range(t,d + 1):
                ans.append(matrix[i][r])
            r -= 1
            if r < l:
                break
            for i in range(r,l-1,-1):
                ans.append(matrix[d][i])
            d -= 1
            if t>d:
                break
            for i in range(d,t-1,-1):
                ans.append(matrix[i][l])
            l += 1
            if r < l:
                break
        return ans



if __name__ == '__main__':
    res = Solution()
    print(res.spiralOrder(matrix))