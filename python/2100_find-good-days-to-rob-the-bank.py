from typing import *

security = [5,3,3,3,5,6,2]
time = 2

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]
        for i in range(1,n):
            if security[i] <= security[i-1]:
                l[i] = l[i-1] + 1
            if security[n-i-1] <= security[n-i]:
                r[n-i-1] = r[n-i] + 1
        ans = []
        for i in range(n):
            if l[i]>=time and r[i]>=time:
                ans.append(i)
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.goodDaysToRobBank(security, time))