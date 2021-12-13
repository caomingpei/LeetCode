class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node: TreeNode):
        if not node:
            return
        self.dfs(node.left)
        if self.prev:
            self.ans = min(abs(self.prev-node.val),self.ans)
        self.prev = node.val
        self.dfs(node.right)

    def minDiffInBST(self, root: TreeNode) -> int:
        self.ans = 0x3f3f3f3f
        self.prev = None
        self.dfs(root)
        return self.ans