# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        if root == None:
            return True
        self.depth(root)
        return self.balanced

    def depth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        x = self.depth(root.left)
        y = self.depth(root.right)
        if abs(x-y) > 1:
            self.balanced = False
        return 1 + max(x,y)