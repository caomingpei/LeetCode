from typing import *
from collections import deque

k = 7

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fi = [1,1]
        while fi[-1] < k:
            fi.append(fi[-1]+fi[-2])
        ans = 0
        i = len(fi)-1
        while k:
            if k >= fi[i]:
                k -= fi[i]
                ans += 1
            i -= 1
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.findMinFibonacciNumbers(k))