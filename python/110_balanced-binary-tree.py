from typing import *
null = None
root = [1,2,2,3,3,null,null,4,4]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ans = True

        def dfs(node):
            nonlocal ans
            if not node or not ans:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            if abs(l-r) > 1:
                ans = False

            return max(l,r) + 1
        dfs(root)
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.isBalanced(root))