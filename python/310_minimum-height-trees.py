from typing import *

n = 4
edges = [[1,0],[1,2],[1,3]]

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        deg = [0 for _ in range(n)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        q = [i for i,d in enumerate(deg) if d == 1]
        remain = n
        while remain>2:
            remain -= len(q)
            cur = q
            q = []
            for x in cur:
                for y in g[x]:
                    deg[y] -= 1
                    if deg[y] == 1:
                        q.append(y)
        return q

if __name__ == '__main__':
    res = Solution()
    print(res.findMinHeightTrees(n,edges))