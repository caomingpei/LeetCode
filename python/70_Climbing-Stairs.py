from typing import *

n = 3

class Mat:
    def __init__(self, n, m):
        self.mat = [[0 for _ in range(m)] for _ in range(n)]

    def __len__(self):
        return len(self.mat)

    def __getitem__(self, item):
        return self.mat[item]

    def multiply(self,a,b):
        c = Mat(len(a),len(a[0]))
        for i in range(len(a)):
            for j in range(len(a[0])):
                c.mat[i][j] = a.mat[i][0] * b.mat[0][j] +a.mat[i][1] * b.mat[1][j]
        return c

    def matpow(self, a, n):
        ret = Mat(2,2)
        ret.mat[0][0] = ret.mat[1][1] = 1
        ret.mat[0][1] = ret.mat[1][0] = 0
        while n > 0:
            if n&1 :
                ret = self.multiply(ret,a)
            n>>=1
            a = self.multiply(a,a)
        return ret


class Solution:
    def climbStairs(self, n: int) -> int:
        ans = Mat(2,2)
        ans.mat[1][1] = 0
        ans.mat[0][0] = ans.mat[0][1] = ans.mat[1][0] = 1
        res = ans.matpow(ans, n)
        return res.mat[0][0]


if __name__ == '__main__':
    res = Solution()
    print(res.climbStairs(n))