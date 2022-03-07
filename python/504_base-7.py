from typing import *

num = -100

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        neg = num < 0
        num = abs(num)
        ans = []
        while num!=0:
            ans.append(str(num % 7))
            num //= 7
        if neg:
            ans.append("-")
        ans.reverse()
        return "".join(ans)

if __name__ == '__main__':
    res = Solution()
    print(res.convertToBase7(num))