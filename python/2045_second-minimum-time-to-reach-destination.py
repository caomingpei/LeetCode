from typing import *
from collections import deque
n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3
change = 5

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        ## t_i = t_i-1 +  t_wait + time
        ## if (t_i-1//change) %2 == 0: twait = 0
        ## else: t_wait = change - t_i % change
        INF = float('inf')
        gra = [[] for _ in range(n+1)]
        for edg in edges:
            x, y = edg[0], edg[1]
            gra[x].append(y)
            gra[y].append(x)
        q = deque()

        ti = [[INF for _ in range(n+1)] for _ in range(2)]
        q.append((1, 0))
        while ti[1][n] == INF:
            ind, t = q.popleft()
            for to in gra[ind]:
                tnext = t + 1
                if tnext < ti[0][to]:
                    ti[1][to] = ti[0][to]
                    ti[0][to] = tnext
                    q.append((to,tnext))
                elif ti[1][to] > tnext and tnext > ti[0][to]:
                    ti[1][to] = tnext
                    q.append((to, tnext))
        ans = 0
        for i in range(ti[1][n]):
            if (ans // change) %2 == 0:
                twait = 0
            else:
                twait = change - ans % change
            ans = ans + time + twait
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.secondMinimum(n,edges, time, change))