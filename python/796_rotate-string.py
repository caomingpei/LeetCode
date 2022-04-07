from typing import *
from collections import deque

s = "abcde"
goal = "cdeab"

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal) or goal not in s+s:
            return False
        return True

if __name__ == '__main__':
    res = Solution()
    print(res.rotateString(s,goal))

