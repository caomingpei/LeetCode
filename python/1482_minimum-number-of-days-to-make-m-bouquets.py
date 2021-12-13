from typing import *


bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        N = len(bloomDay)
        if m*k > N:
            return -1
        minday = 0
        maxday = 1
        for i in range(N):
            maxday = max(maxday,bloomDay[i])

        def check(miday):
            bucket = 0
            cur = 0
            for i in range(N):
                if bloomDay[i] <= miday:
                    cur += 1
                else:
                    cur = 0
                if cur == k:
                    bucket += 1
                    cur = 0
            if bucket >= m:
                return True
            return False
        ans = 0

        while minday <= maxday:
            mid = int((minday+maxday)/2)
            if check(mid):
                ans = mid
                maxday = mid - 1
            else:
                minday = mid + 1

        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.minDays(bloomDay,m,k))