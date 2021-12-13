from typing import *
graph = [[1,2,3],[0],[0],[0]]

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        mat = [[float('inf') for _ in range(N)] for _ in range(N)]
        for i in range(N):
            mat[i][i] = 0
            for j in graph[i]:
                mat[i][j] = 1
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

        dp = [[float('inf') for _ in range(N)] for _ in range(1<<N + 1)]
        for i in range(N):
            dp[1<<i][i] = 0
        for i in range(1<<N):
            for j in range(N):
                if i & (1<<j) != 0:
                    for k in range(N):
                        if i & (1<<k) != 0:
                            dp[i][j] = min(dp[i][j], mat[j][k]+dp[i^(1<<j)][k])

        return int(min(x for x in dp[(1<<N) -1]))

if __name__ == '__main__':
    res = Solution()
    print(res.shortestPathLength(graph))