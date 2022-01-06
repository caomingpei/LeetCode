from typing import *
from collections import deque
path="/hello../world"

class Solution:
    def simplifyPath(self, path: str) -> str:
        pathlis = path.split("/")
        stk = deque()
        for name in pathlis:
            if name == "..":
                if stk:
                    stk.pop()
            elif name and name !='.':
                stk.append(name)

        return "/" + "/".join(stk)




if __name__ == '__main__':
    res = Solution()
    print(res.simplifyPath(path))

