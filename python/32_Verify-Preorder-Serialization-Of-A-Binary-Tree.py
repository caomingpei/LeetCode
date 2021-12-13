from typing import *
s = "9,3,4,#,#,1,#,#,2,#,6,#,#"

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        mystack = []
        for letter in preorder.split(','):
            mystack.append(letter)
            while len(mystack) > 2 and mystack[-1] == mystack[-2] == '#' and mystack[-3] != '#':
                mystack.pop(), mystack.pop(), mystack.pop()
                mystack.append('#')

        if len(mystack) == 1 and mystack[-1] == '#':
            return True
        else:
            return False

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        diff = 1
        for node in preorder.split(','):
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2
        if diff == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    res = Solution()
    print(res.isValidSerialization(s))