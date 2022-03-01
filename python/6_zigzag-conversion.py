from typing import *

s = "PAYPALISHIRING"
numRows = 4

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r==1 or r>=n:
            return s
        t = 2*r - 2
        ans = []
        for i in range(r):
            j = 0
            while j+i<n:
                ans.append(s[j+i])
                if (0<i and i<r-1) and j+t-i<n:
                    ans.append(s[j+t-i])
                j += t
        return "".join(ans)


if __name__ == '__main__':
    res = Solution()
    print(res.convert(s,numRows))