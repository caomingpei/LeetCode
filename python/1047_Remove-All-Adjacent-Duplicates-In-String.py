from typing import *
S = "abbaca"

class Solution:
    def removeDuplicates(self, S: str) -> str:
        ans = []
        for i in range(len(S)):
            if len(ans) and ans[-1] == S[i]:
                ans.pop()
            else:
                ans.append(S[i])
        return ''.join(ans)

if __name__ == '__main__':
    res = Solution()
    print(res.removeDuplicates(S))