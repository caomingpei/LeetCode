from typing import *
import heapq

left = 1
right = 22

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right+1):
            cur = num
            flag = 1
            while cur:
                thc = cur % 10
                cur //= 10
                if thc == 0 or num % thc !=0:
                    flag = 0
                    break
            if flag:
                ans.append(num)
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.selfDividingNumbers(left, right))