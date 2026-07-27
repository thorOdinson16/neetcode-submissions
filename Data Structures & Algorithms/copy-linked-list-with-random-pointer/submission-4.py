"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        x = {}
        start = head
        if head == None:
            return None
        target = Node(head.val)
        x[head] = target
        head = head.next
        ans = target
        while head!= None:
            new = Node(head.val)
            target.next = new
            x[head] = new
            target = target.next
            head = head.next
        target = ans
        while start!= None:
            if start.random == None:
                x[start].random = None
            else:
                y = start.random
                x[start].random = x[y]
            start = start.next
        return ans