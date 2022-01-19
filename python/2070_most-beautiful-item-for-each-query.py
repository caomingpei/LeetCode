from typing import *

items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        vmax = 0
        for i in range(len(items)):
            vmax = max(vmax, items[i][1])
            items[i][1] = vmax

        ans = []
        for i in range(len(queries)):
            query = queries[i]
            l = 0
            r = len(items) - 1
            ind = 0
            while l <= r:
                mid = (l+r)//2
                if items[mid][0] <= query:
                    l = mid + 1
                    ind = mid
                else:
                    r = mid - 1
            if items[ind][0] <= query:
                ans.append(items[ind][1])
            else:
                ans.append(0)

        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.maximumBeauty(items, queries))