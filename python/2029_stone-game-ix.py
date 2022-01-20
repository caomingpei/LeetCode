import sys
from typing import *
from collections import deque

stones = [77,74,12,63,95,23,19,91,48,87,26,22,21,30,41,10,22,80,14,36,62,29,13,3,15,47,71,1,95,21,43,84,62,70,10,86,70,9,38,30,51,32,75,87,73,8,54,64,35,22,68,75,4,59,69,82,27,9,20,32,64,59,58,48,32,21,15,20,75]


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cals = [0,0,0]
        for i in range(len(stones)):
            cals[stones[i] % 3] += 1
        if cals[0] %2 == 0:
            if cals[1] == 0 or cals[2] == 0:
                return False
            else:
                return True
        else:
            diffnum = abs(cals[1] - cals[2])
            if diffnum <= 2:
                return False
            else:
                return True


if __name__ == '__main__':
    res = Solution()
    print(res.stoneGameIX(stones))