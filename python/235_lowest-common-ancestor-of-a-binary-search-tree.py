from typing import *
null = None
root = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if ancestor.val < p.val and ancestor.val < q.val:
                ancestor = ancestor.right
            elif ancestor.val > p.val and ancestor.val > q.val:
                ancestor = ancestor.left
            else:
                break
        return ancestor


if __name__ == '__main__':
    res = Solution()
    print(res.lowestCommonAncestor(root, p, q))