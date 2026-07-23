# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        c = 0
        curr = head
        while curr != None:
            l += 1
            curr = curr.next
        if l == 1:
            head = None
            return head
        r = l - n
        prev = None
        curr = head
        if r == 0:
            prev = curr
            curr = curr.next
            prev.next = None
            head = curr
            return head
        while c != r and curr!=None:
            prev = curr
            curr = curr.next
            c += 1
        prev.next = curr.next
        curr.next = None
        return head