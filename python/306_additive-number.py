from typing import *

num = "199100199"

class Solution:
    def generate(self, num, i, j):
        if len(num[:i]) >= 2 and num[0] == '0': return ""
        if len(num[i:j]) >= 2 and num[i] == '0': return ""

        a = int(num[:i])
        b = int(num[i:j])
        ans = num[:j]
        while len(ans) < len(num):
            a, b = b, a + b
            ans += str(b)
        return ans

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n-1):
            for j in range(i+1, n):
                if self.generate(num,i,j) == num:
                    return True
        return False


if __name__ == '__main__':
    res = Solution()
    print(res.isAdditiveNumber(num))