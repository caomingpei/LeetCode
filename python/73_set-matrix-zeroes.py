from typing import *

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flag_row, flag_col = False, False
        N = len(matrix)
        M = len(matrix[0])

        for i in range(N):
            if matrix[i][0] == 0:
                flag_col = True

        for j in range(M):
            if matrix[0][j] == 0:
                flag_row = True

        for i in range(1,N):
            for j in range(1,M):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, N):
            if matrix[i][0] == 0:
                for j in range(1, M):
                    matrix[i][j] = 0

        for j in range(1, M):
            if matrix[0][j] == 0:
                for i in range(1, N):
                    matrix[i][j] = 0

        if flag_col:
            for i in range(N):
                matrix[i][0] = 0

        if flag_row:
            for j in range(M):
                matrix[0][j] = 0


if __name__ == '__main__':
    res = Solution()
    print(res.setZeroes())