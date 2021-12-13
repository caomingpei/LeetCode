# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        idx = inorder.index(node.val)
        node.left = self.buildTree(preorder[1:idx+1],inorder[:idx])
        node.right = self.buildTree(preorder[idx+1:],inorder[idx+1:])