# Last updated: 5/6/2025, 1:43:05 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next # Save the next of current
            curr.next = prev # Link current to previous
            # Update Pointers
            prev = curr # Set previous to current
            curr = temp # Set current to next
        return prev

        
        