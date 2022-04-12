from typing import *

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        cur = 0
        row = 1
        for i in range(len(s)):
            nowlen = widths[ord(s[i])-ord('a')]
            if cur+nowlen >100:
                row += 1
                cur = nowlen
            else:
                cur += nowlen
        return [row,cur]

if __name__ == '__main__':
    res = Solution()
    print(res.numberOfLines(widths,S))