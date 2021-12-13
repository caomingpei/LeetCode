from typing import *

citations = [1]

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0 for _ in range(n+1)]
        presum = [0 for _ in range(n+1)]
        for c in citations:
            num = n if c > n else c
            count[num] += 1
        presum[n] = count[n]
        for i in range(n-1, -1, -1):
            presum[i] = presum[i+1] + count[i]
        ans = 0
        for i in range(n+1):
            if presum[i] >= i:
                ans = i
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.hIndex(citations))