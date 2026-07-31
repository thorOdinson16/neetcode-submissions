# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None or subRoot == None:
            return False
        if root.val == subRoot.val:
            z = self.isSameTree(root, subRoot)
            if z == True:
                return z
            else:
                z1 = self.isSubtree(root.left, subRoot)
                z2 = self.isSubtree(root.right, subRoot)
                return (z1 or z2)
        else:
            z1 = self.isSubtree(root.left, subRoot)
            z2 = self.isSubtree(root.right, subRoot)
            return (z1 or z2)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif (p != None and q == None) or (p == None and q!= None):
            return False
        if p.val == q.val:
            x = self.isSameTree(p.left, q.left)
            y = self.isSameTree(p.right, q.right)
            return x and y
        else:
            return False