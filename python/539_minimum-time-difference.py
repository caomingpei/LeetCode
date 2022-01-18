from typing import *
timePoints = ["00:00","23:59"]


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        milis = [0 for _ in range(24*60)]
        THISMAX = 24*60
        fir = THISMAX
        last = -1
        if len(timePoints) > THISMAX:
            return 0
        for i in range(len(timePoints)):
            time = timePoints[i]
            hr,minu = time.split(":")
            curminu = 60*int(hr) + int(minu)
            milis[curminu] += 1
            fir = min(fir, curminu)
            last = max(last, curminu)

        ans = THISMAX + fir - last
        li = -1
        for i in range(len(milis)):
            if milis[i] > 1:
                ans = 0
            elif milis[i] > 0:
                if li != -1:
                    ans = min(ans,i-li)
                li = i
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.findMinDifference(timePoints))

