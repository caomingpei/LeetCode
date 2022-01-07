from typing import *
from collections import deque

original = [1,2,3,4]
m = 2
n = 2


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(len(original)):
            ans[int(i/n)][i%n] = original[i]
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.construct2DArray(original,m,n))