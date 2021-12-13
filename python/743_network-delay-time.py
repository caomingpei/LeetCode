from typing import *
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dic = {i:float('inf') for i in range(1,n+1)}
        dic[k] = 0
        ans = {}
        while dic:
            curmin = float('inf')
            ind = -1
            for k, v in dic.items():
                if curmin > v:
                    curmin = v
                    ind = k
            for time in times:
                if time[0] == ind  and time[1] not in ans.keys():
                    dic[time[1]] = min(dic[time[1]], dic[time[0]] + time[2])
            if curmin == float('inf'):
                return -1
            ans[ind] = curmin
            dic.pop(ind)
        return max(ans.values())


if __name__ == '__main__':
    res = Solution()
    print(res.networkDelayTime(times, n, k))