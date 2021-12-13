from typing import *

intervals = [[1,4],[2,3]]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda x: x[0])
        le = len(intervals)
        lind = -1
        rind = -1
        ans = []
        for i in range(le):
            print(lind,rind,i)
            if lind == -1:
                lind = intervals[i][0]
                rind = intervals[i][1]
            else:
                if intervals[i][0] <= rind:
                    rind = max(intervals[i][1],rind)
                else:
                    ans.append([lind, rind])
                    lind = intervals[i][0]
                    rind = intervals[i][1]
        ans.append([lind, rind])
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.merge(intervals))