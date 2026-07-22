# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = head
        curr = head.next
        prev.next = None
        while curr != None:
            head = curr
            temp = curr.next
            curr.next = prev
            curr = temp
            prev = head
        return head