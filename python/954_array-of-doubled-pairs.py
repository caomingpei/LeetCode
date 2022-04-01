from typing import *
from collections import Counter
arr = [1,2,4,8]

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        if cnt[0]%2:
            return False
        for cur in sorted(cnt,key=lambda x:abs(x)):
            if cnt[2*cur] < cnt[cur]:
                return False
            cnt[2*cur] -= cnt[cur]
        return True

if __name__ == '__main__':
    res = Solution()
    print(res.canReorderDoubled(arr))