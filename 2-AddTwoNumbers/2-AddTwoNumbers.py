# Last updated: 6/5/2025, 8:34:01 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(0)
        current = newList
        carry = 0

        while l1 or l2:        
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            if total >= 10:
                carry = 1
                total = total % 10
            else:
                carry = 0
            
            current.next = ListNode(total)
            current  = current.next

            if l1 is not None and l2 is None:
                l1 = l1.next
            elif l2 is not None and l1 is None:
                l2 = l2.next
            else:
                l1 = l1.next
                l2 = l2.next

        if carry == 1:
            current.next = ListNode(carry)
            current  = current.next

        return newList.next
            


        