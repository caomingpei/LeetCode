from typing import *
from collections import defaultdict

n = 5
lamps = [[0,0],[0,4]]
queries = [[0,4],[0,1],[1,4]]

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamps_set = set()
        for i in range(len(lamps)):
            x, y = lamps[i]
            lamps_set.add((x, y))

        row, col, dia, antidia = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        def prolampset(x, y, num):
            row[x] += num
            col[y] += num
            dia[x - y] += num
            antidia[x + y] += num
        for lx, ly in lamps_set:
            prolampset(lx,ly, 1)

        ans = []
        ori = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
        for query in queries:
            curx, cury = query
            if row[curx]>0 or col[cury]>0 or dia[curx-cury]>0 or antidia[curx+cury]>0:
                ans.append(1)
                for o in ori:
                    nx = curx + o[0]
                    ny = cury + o[1]
                    if nx<0 or nx>=n or ny<0 or ny>=n or (nx, ny) not in lamps_set:
                        continue
                    else:
                        lamps_set.remove((nx, ny))
                        prolampset(nx, ny, -1)
            else:
                ans.append(0)

        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.gridIllumination(n, lamps, queries))