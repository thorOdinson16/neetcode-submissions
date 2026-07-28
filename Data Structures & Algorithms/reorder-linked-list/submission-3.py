# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return None
        slow = head
        fast = head.next
        while fast!=None and fast.next!=None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None
        while curr != None:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead
        while head != None:
            if prev == None:
                break
            new = head.next
            head.next = prev
            new2 = prev.next
            prev.next = new
            prev = new2
            head = new
        return None