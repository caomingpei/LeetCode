from typing import *
n = 4


class Solution:
    def gcd(self,a,b):
        while b:
            t = b
            b = a % b
            a = t
        return a

    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []
        s = set()
        for i in range(1,n+1):
            for j in range(1,i):
                mnum = self.gcd(i,j)
                s.add(str(int(j/mnum))+"/"+str(int(i/mnum)))
        ans = list(s)
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.simplifiedFractions(n))

