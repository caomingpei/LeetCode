from typing import *
null = None
root = [1,2,3,null,5]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def init(self):
        self.ans = []

    def dfs(self, node, path):
        if node:
            path += str(node.val)
            if not node.left and not node.right:
                self.ans.append(path)
            else:
                path += "->"
                self.dfs(node.left, path)
                self.dfs(node.right, path)
        return

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.init()
        self.dfs(root,"")
        return self.ans


if __name__ == '__main__':
    res = Solution()
    print(res.binaryTreePaths(root))