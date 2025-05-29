# Last updated: 5/28/2025, 10:11:13 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = head
        s = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if s == f:
                return True

        return False