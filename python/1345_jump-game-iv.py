from typing import *
from collections import deque

arr = [51,64,-15,58,98,31,48,72,78,-63,92,-5,64,-64,51,-48,64,48,-76,-86,-5,-64,-86,-47,92,-41,58,72,31,78,-15,-76,72,-5,-97,98,78,-97,-41,-47,-86,-97,78,-97,58,-41,72,-41,72,-25,-76,51,-86,-65,78,-63,72,-15,48,-15,-63,-65,31,-41,95,51,-47,51,-41,-76,58,-81,-41,88,58,-81,88,88,-47,-48,72,-25,-86,-41,-86,-64,-15,-63]

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n =len(arr)
        if len(arr) == 1:
            return 0
        dicind = {}
        INF = float('inf')
        dist = [INF for _ in range(n)]
        for i in range(len(arr)):
            if arr[i] not in dicind.keys():
                dicind[arr[i]] = [i]
            else:
                dicind[arr[i]].append(i)
        que = deque([0])
        dist[0] = 0

        def bfs():
            while que:
                ind = que.popleft()
                depth = dist[ind]
                ## print(ind,arr[ind],depth)
                if ind == n-1:
                    return depth
                if arr[ind] in dicind.keys():
                    for eqnum in dicind[arr[ind]]:
                        if dist[eqnum] == INF:
                            dist[eqnum] = depth + 1
                            que.append(eqnum)
                    dicind.pop(arr[ind])
                if dist[ind + 1] == INF and ind + 1 < n:
                    dist[ind + 1] = depth + 1
                    que.append(ind + 1)
                if dist[ind - 1] == INF and ind - 1 >= 0:
                    dist[ind - 1] = depth + 1
                    que.append(ind - 1)
            return -1

        ans = bfs()
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.minJumps(arr))