from typing import *
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        myqueue = deque()
        rootpair = (-1,root,0)
        myqueue.append(rootpair)
        xenv = False
        yenv = False
        while len(myqueue):
            parent, node, count = myqueue.popleft()
            if node.val == x:
                xenv = (parent, count)
            elif node.val == y:
                yenv = (parent, count)
            if xenv and yenv:
                break
            if node.left != None:
                myqueue.append((node.val, node.left, count + 1))
            if node.right != None:
                myqueue.append((node.val, node.right, count + 1))

        if xenv and yenv:
            if xenv[1] == yenv[1] and xenv[0] != yenv[0]:
                return True
        return False

if __name__ == '__main__':
    res = Solution()
    print(res.isCousins())