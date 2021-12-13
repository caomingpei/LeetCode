from typing import *
x = 1534236469

class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if(x>=0):
            lis = list(str(x))
            lis.reverse()
            ans = int(''.join(lis))
        else:
            lis = list(str(x))
            lis = lis[1:]
            lis.reverse()
            ans = 0-int(''.join(lis))
        return ans if  -2147483648 < ans < 2147483647 else 0


if __name__ == '__main__':
    res = Solution()
    print(res.reverse(x))

