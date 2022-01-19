from typing import *
k = 3
n = 9


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        numlis = [1,2,3,4,5,6,7,8,9]
        ans = []
        visited = {}
        def dfs(curlis, depth):
            if depth == k:
                cur = []
                for i in range(len(curlis)):
                    if curlis[i] == 1:
                       cur.append(numlis[i])
                if sum(cur) == n:
                    ans.append(cur)
            for i in range(len(curlis)):
                nxcurlis = curlis[:]
                if nxcurlis[i] == 0:
                    nxcurlis[i] = 1
                if tuple(nxcurlis) not in visited.keys():
                    visited[tuple(nxcurlis)] = True
                    dfs(nxcurlis, depth+1)
        dfs([0 for _ in range(9)], 0)
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.combinationSum3(k, n))

