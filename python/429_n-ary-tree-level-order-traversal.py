from typing import *
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append((root,0))
        ans = [[]]
        while q:
            cur,dep = q.popleft()
            if len(ans) < dep + 1:
                ans.append([cur.val])
            else:
                ans[dep].append(cur.val)
            for ch in cur.children:
                q.append((ch, dep+1))
        return ans