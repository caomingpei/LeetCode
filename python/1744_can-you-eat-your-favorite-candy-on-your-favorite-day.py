from typing import *
candiesCount = [7,4,5,3,8]
queries = [[0,2,2],[4,2,4],[2,13,1000000000]]


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        presum = [0 for _ in range(len(candiesCount))]
        presum[0] = candiesCount[0]
        for i in range(1,len(candiesCount)):
            presum[i] = presum[i-1] + candiesCount[i]
        ans = [False for _ in range(len(queries))]
        for i in range(len(queries)):
            query = queries[i]
            favT, favD, daCap = query[0], query[1], query[2]
            candAll = presum[favT]
            if favT == 0 and candAll >= favD + 1:
                ans[i] = True
                continue
            lastAll = presum[favT-1]
            if not (candAll < favD + 1 or lastAll >= (favD+1)*daCap):
                ans[i] = True
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.canEat(candiesCount, queries))

