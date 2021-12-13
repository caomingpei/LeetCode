from typing import *

mat = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
target = 5
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = m-1
        flag = matrix[i][j]
        while (i < n) and (j > -1):
            if target > flag:
                i += 1
                if i == n:
                    break
                flag = matrix[i][j]
            elif target < flag:
                j -= 1
                if j == -1:
                    break
                flag = matrix[i][j]
            else:
                return True
        return False
if __name__ == '__main__':
    res = Solution()
    print(res.findNumberIn2DArray(mat,target))