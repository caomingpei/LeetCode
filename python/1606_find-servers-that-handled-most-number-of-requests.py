from typing import *
import heapq
k = 6
arrival =[1,2,3,9,11,12,14]
load = [12,3,8,13,6,10,14]

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        process = [0 for _ in range(k)]
        available = list(range(k))
        busy = []

        for i in range(len(arrival)):
            start = arrival[i]
            execute = load[i]

            while busy and busy[0][0] <= start:
                _, id = heapq.heappop(busy)
                heapq.heappush(available,i + ((id - i)%k+k)%k)

            if available:
                id = heapq.heappop(available) %k
                process[id] += 1
                heapq.heappush(busy,(start+execute, id))

        max_cnt = max(process)
        return [i for i, item in enumerate(process) if item == max_cnt]

if __name__ == '__main__':
    res = Solution()
    print(res.busiestServers(k,arrival,load))