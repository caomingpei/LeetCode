from typing import *
S = "]"
from collections import deque

class Solution:
    lis = ['(', '[', '{']
    dic = {')':'(', ']':'[', '}':'{'}
    def isValid(self, s: str) -> bool:
        mystack = deque()
        flag = 1
        for cha in s:
            if cha in self.lis:
                mystack.append(cha)
            else:
                if len(mystack):
                    top = mystack[-1]
                    if self.dic[cha] == top:
                        mystack.pop()
                    else:
                        flag = 0
                else:
                    flag = 0
            if flag == 0:
                break
        if flag and len(mystack)==0:
            return True
        else:
            return False

if __name__ == '__main__':
    res = Solution()
    print(res.isValid(S))


