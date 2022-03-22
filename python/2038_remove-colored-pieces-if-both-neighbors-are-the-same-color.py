from typing import *

colors = "AAABABB"

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        num = [0,0]
        cur = ""
        cnt = 0
        for c in colors:
            if c != cur:
                cur = c
                cnt = 1
            else:
                cnt += 1
            if cnt >=3:
                num[ord(cur) - ord("A")] += 1
        if num[0] > num[1]:
            return True
        return False


if __name__ == '__main__':
    res = Solution()
    print(res.winnerOfGame(colors))