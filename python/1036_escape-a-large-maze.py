from typing import *
from collections import deque

blocked = [[0,999991],[0,999993],[0,999996],[1,999996],[1,999997],[1,999998],[1,999999]]
source = [0,999997]
target = [0,2]

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if len(blocked) < 2:
            return True
        BOUNDRY = 10**6 -1
        blocked_row = [pos[0] for pos in blocked]
        blocked_row.extend([source[0],target[0]])

        blocked_col = [pos[1] for pos in blocked]
        blocked_col.extend([source[1], target[1]])
        row = sorted(blocked_row)
        col = sorted(blocked_col)

        r_dict, c_dict = dict(), dict()
        r_id = (0 if row[0] == 0 else 1)
        r_dict[row[0]] = r_id
        for i in range(1,len(row)):
            if row[i] - row[i-1] == 1:
                r_id += 1
            elif row[i] - row[i-1] > 1:
                r_id += 2
            r_dict[row[i]] = r_id
        if row[-1] != BOUNDRY:
            r_id += 1

        c_id = (0 if col[0] == 0 else 1)
        c_dict[col[0]] = c_id
        for i in range(1, len(col)):
            if col[i] - col[i - 1] == 1:
                c_id += 1
            elif col[i] - col[i - 1] > 1:
                c_id += 2
            c_dict[col[i]] = c_id
        if col[-1] != BOUNDRY:
            c_id += 1

        grid = [[0 for _ in range(c_id + 1)] for _ in range(r_id + 1)]
        for i in range(len(blocked)):
            cur = blocked[i]
            grid[r_dict[cur[0]]][c_dict[cur[1]]] = 1

        sx,sy = r_dict[source[0]], c_dict[source[1]]
        ex,ey = r_dict[target[0]], c_dict[target[1]]

        q = deque([(sx,sy)])
        grid[sx][sy] = 1
        ori = [[0,1], [1,0], [0,-1], [-1,0]]
        while q:
            x, y = q.popleft()
            for dx,dy in ori:
                nx = x+dx
                ny = y+dy
                if 0<=nx and nx <=r_id and 0<=ny and ny <=c_id and grid[nx][ny]==0:
                    if (nx, ny) == (ex, ey):
                        return True
                    q.append((nx,ny))
                    grid[nx][ny] = 1
        return False


if __name__ == '__main__':
    res = Solution()
    print(res.isEscapePossible(blocked, source, target))