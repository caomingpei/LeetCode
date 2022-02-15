from typing import *
from collections import defaultdict

matrix = [[3,7,8],[9,11,13],[15,16,17]]
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        min_row = [0 for _ in range(m)]
        min_col = [0 for _ in range(n)]
        for i in range(m):
            cur = float("inf")
            for j in range(n):
                cur = min(cur, matrix[i][j])
            min_row[i] = cur

        for j in range(n):
            cur = 0
            for i in range(m):
                cur = max(cur, matrix[i][j])
            min_col[j] = cur

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == min_row[i] and matrix[i][j] == min_col[j]:
                    ans.append(matrix[i][j])

        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.luckyNumbers(matrix))