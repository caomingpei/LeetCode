from typing import *

matrix = [[1,1]]
target = 2

class Solution:
    def bisearch(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        l1 = 0
        r1 = n-1
        ans1 = -1
        while(l1 <= r1):
            mid = int((l1 + r1) / 2)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l1 = mid + 1
                ans1 = mid
            else:
                r1 = mid - 1
        matlis = matrix[ans1]
        l2 = 0
        r2 = m-1
        while(l2 <= r2):
            mid = int((l2 + r2) / 2)
            if matlis[mid] == target:
                return True
            elif matlis[mid] < target:
                l2 = mid + 1
            else:
                r2 = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.bisearch(matrix,target)

if __name__ == '__main__':
    res = Solution()
    print(res.searchMatrix(matrix,target))