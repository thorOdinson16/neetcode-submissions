# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None:
            return None
        if root == p or root == q:
            return root
        else:
            x = self.lowestCommonAncestor(root.left, p, q)
            y = self.lowestCommonAncestor(root.right, p, q)
            if x == None and y == None:
                return None
            elif x != None and y == None:
                return x
            elif x == None and y != None:
                return y
            elif x != None and y != None:
                return root