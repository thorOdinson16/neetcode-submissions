# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        x = set()
        if head == None:
            return False
        while head.next != None:
            if head.val in x:
                return True
            else:
                x.add(head.val)
            head = head.next
        return False
