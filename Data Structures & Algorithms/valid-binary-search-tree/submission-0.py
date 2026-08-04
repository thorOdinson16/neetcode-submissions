# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], less, more) -> bool:
            if root == None:
                return True
            if root.val <= less or root.val >= more:
                return False
            x = dfs(root.left, less, root.val)
            y = dfs(root.right, root.val, more)
            return x and y
        return dfs(root, float('-inf'), float('inf'))