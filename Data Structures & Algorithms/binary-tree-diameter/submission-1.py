# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        if root == None:
            return 0
        self.depth(root)
        return self.ans

    def depth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        x = self.depth(root.left)
        y = self.depth(root.right)
        if (x+y) > self.ans:
            self.ans = x+y
        return 1 + max(x,y)