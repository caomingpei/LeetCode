from typing import *
s = "We are happy."

class Solution:
    def replaceSpace(self, s: str) -> str:
        ans = []
        for st in s:
            if st == ' ':
                ans.append('%20')
            else:
                ans.append(st)
        return "".join(ans)

if __name__ == '__main__':
    res = Solution()
    print(res.replaceSpace(s))