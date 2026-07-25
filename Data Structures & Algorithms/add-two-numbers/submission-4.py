# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l2
        carry = []
        prev = None
        while l1 != None and l2 != None:
            l2.val = l1.val + l2.val
            if len(carry) != 0:
                l2.val += 1
                carry.pop()
            if l2.val > 9:
                l2.val = (l2.val%10)
                carry.append(1)
            l1 = l1.next
            prev = l2
            l2 = l2.next
        if l1 != None:
            while l1!=None:
                new = ListNode()
                new.val = l1.val
                if len(carry) != 0:
                    new.val += 1
                    carry.pop()
                if new.val > 9:
                    new.val = (new.val%10)
                    carry.append(1)
                prev.next = new
                l1 = l1.next
                prev = prev.next
        if l2 != None:
            while l2 != None:
                new = ListNode()
                new.val = l2.val
                if len(carry) != 0:
                    new.val += 1
                    carry.pop()
                if new.val > 9:
                    new.val = (new.val%10)
                    carry.append(1)
                prev.next = new
                l2 = l2.next
                prev = prev.next
        if len(carry)!=0:
            node = ListNode()
            prev.val = (prev.val%10)
            prev.next = node
            node.val = 1
        return head