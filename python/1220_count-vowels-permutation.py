from typing import *
n = 5


class Solution:
    def __init__(self):
        self.matrix =[[0,1,1,0,1],
                      [1,0,1,0,0],
                      [0,1,0,1,0],
                      [0,0,1,0,0],
                      [0,0,1,1,0]
                      ]
        self.f1 = [1,1,1,1,1]
        self.MOD = int(1e9 + 7)

    def matdow(self, t1, t2):
        n1,m1 = len(t1), len(t1[0])
        n2,m2 = len(t2), len(t2[0])
        assert (n1==n2) and (m1==m2) and (n1 == m1)
        ret = [[0 for _ in range(n1)] for _ in range(n1)]
        for i in range(n1):
            for j in range(n1):
                for k in range(n1):
                    ret[i][j] += t1[i][k] * t2[k][j]
                ret[i][j] = ret[i][j] % self.MOD
        return ret


    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        fn = n-1
        A = [[1 if(i==j) else 0 for i in range(len(self.matrix))] for j in range(len(self.matrix))]
        while fn:
            if fn % 2==0:
                self.matrix = self.matdow(self.matrix, self.matrix)
                fn /= 2
            else:
                A = self.matdow(A,self.matrix)
                fn -= 1
        ans = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                ans += A[i][j]
        return ans % self.MOD

if __name__ == '__main__':
    res = Solution()
    print(res.countVowelPermutation(n))

