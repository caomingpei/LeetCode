from typing import *
from collections import deque
from heapq import *
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m,n = len(nums1),len(nums2)
        ans = []
        pq = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()
        while pq and len(ans) < k:
            _, i, j = heappop(pq)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            ans.append([nums1[i], nums2[j]])
            if i + 1 < m:
                heappush(pq, (nums1[i+1] + nums2[j], i + 1, j))
            if j + 1 < n:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.kSmallestPairs(nums1,nums2,k))

