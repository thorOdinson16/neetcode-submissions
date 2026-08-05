# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def inorder(root: Optional[TreeNode]) -> int:
            if root == None:
                return -1
            x = inorder(root.left)
            if x != None and x > -1:
                return x
            self.k -= 1
            if self.k == 0:
                return root.val
            y = inorder(root.right)
            if y != None and y > -1:
                return y
        return inorder(root)
