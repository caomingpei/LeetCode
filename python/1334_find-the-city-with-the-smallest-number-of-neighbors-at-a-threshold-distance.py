from typing import *
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4


class Solution:
    INTMAX = 0x3f3f3f3f
    def init(self, n, edges):
        self.mat = [ [self.INTMAX for _ in range(n)] for _ in range(n)]
        for i in range(len(edges)):
            x = edges[i][0]
            y = edges[i][1]
            w = edges[i][2]
            self.mat[x][y] = w
            self.mat[y][x] = w
        for i in range(0,n):
            self.mat[i][i] = 0
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        self.init(n,edges)
        for k in range(0,n):
            for i in range(0,n):
                for j in range(0,n):
                    if self.mat[i][j] > self.mat[i][k] + self.mat[k][j]:
                        self.mat[i][j] = self.mat[i][k] + self.mat[k][j]
                        #self.mat[j][i] = self.mat[i][j]

        mincitynum = self.INTMAX
        ansind = 0
        for i in range(0,n):
            curnum = 0
            for j in range(0,n):
                if self.mat[i][j] <= distanceThreshold:
                    curnum += 1
            #print(i,curnum)
            if curnum <= mincitynum:
                mincitynum = curnum
                ansind = i
        return ansind
if __name__ == '__main__':
    res = Solution()
    print(res.findTheCity(n, edges, distanceThreshold))