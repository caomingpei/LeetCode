from typing import *
num = 16

class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]*(num+1)
        for i in range(1,num+1):
            ans[i] = ans[i >> 1] + i%2

        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.countBits(num))

    ## 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    ## 0 1 1 2 1 2 2 3 1 2  2  3  2  3  3  4  1
