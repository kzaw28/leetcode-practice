# Last updated: 7/8/2025, 8:12:54 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Cycle detecting = Fast/ Slow pointer
        slow = head  
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Find the head
                res = head
                while res != slow:
                    res = res.next
                    slow = slow.next
                return res

        return None
        