from typing import *
from collections import deque

s = "(1)+((2))+(((3)))"

class Solution:
    def maxDepth(self, s: str) -> int:
        stk = deque()
        ans = 0
        cur = 0
        for chr in s:
            if chr == "(":
                cur += 1
                ans = max(cur, ans)
                stk.append(chr)
            elif chr == ")":
                if stk[-1] == "(":
                    cur -= 1
                    stk.pop()
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.maxDepth(s))