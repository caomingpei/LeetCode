from typing import *
from collections import deque

properties = [[1,5],[10,4],[10,3],[4,3]]

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        ans = 0
        maxD = 0
        for i, val in enumerate(properties):
            if val[1] < maxD:
                ans += 1
            else:
                maxD = max(maxD, val[1])
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.numberOfWeakCharacters(properties))