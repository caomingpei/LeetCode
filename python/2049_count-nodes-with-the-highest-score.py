from typing import *
from collections import deque
from collections import defaultdict
parents = [-1,2,0,2,0]

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        children = defaultdict(list)
        n = len(parents)
        for i,p in enumerate(parents):
            if p != -1:
                children[p].append(i)

        cnt = [0 for _ in range(n)]
        def dfs(ind):
            if cnt[ind] > 0: return cnt[ind]
            cnt[ind] = 1
            for ch in children[ind]:
                cnt[ind] += dfs(ch)
            return cnt[ind]

        dfs(0)
        mmax, ans = 0,0

        for i in range(n):
            lis = children[i]
            cur = 1
            if len(lis) == 1:
                cur = cnt[lis[0]] * 1
            elif len(lis) == 2:
                cur = cnt[lis[0]] * cnt[lis[1]]

            if parents[i] != -1:
                cur *= n-cnt[i]
            if cur > mmax:
                mmax = cur
                ans = 1
            elif cur == mmax:
                ans += 1

        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.countHighestScoreNodes(parents))