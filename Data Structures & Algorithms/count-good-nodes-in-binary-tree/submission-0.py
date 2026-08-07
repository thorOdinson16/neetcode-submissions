# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 1
        q = deque()
        q.append((root, root.val))
        while len(q) > 0:
            x = q.popleft()
            if x[0].left:
                if x[0].left.val >= x[1]:
                    good += 1
                    q.append((x[0].left, x[0].left.val))
                else:
                    q.append((x[0].left, x[1]))
            if x[0].right:
                if x[0].right.val >= x[1]:
                    good += 1
                    q.append((x[0].right, x[0].right.val))
                else:
                    q.append((x[0].right, x[1])) 
        return good   
        