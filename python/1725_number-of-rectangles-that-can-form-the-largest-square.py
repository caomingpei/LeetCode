from typing import *
from collections import deque
from collections import defaultdict

rectangles = [[5,8],[3,9],[5,12],[16,5]]
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        caldic = defaultdict(int)
        for i in range(len(rectangles)):
            l,w = rectangles[i]
            caldic[min(l,w)] += 1
        ans = 0
        for k in caldic.keys():
            ans = max(ans,k)
        return caldic[ans]


if __name__ == '__main__':
    res = Solution()
    print(res.countGoodRectangles(rectangles))