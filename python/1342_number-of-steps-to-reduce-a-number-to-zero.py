from typing import *
from collections import deque

num = 14

class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            if num %2 ==0:
                num /= 2
                ans += 1
            else:
                num -= 1
                ans += 1
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.numberOfSteps(num))