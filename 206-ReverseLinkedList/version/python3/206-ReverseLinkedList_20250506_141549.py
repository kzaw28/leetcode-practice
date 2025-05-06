# Last updated: 5/6/2025, 2:15:49 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # BASE CASE
        # If head is the last node, return head (e.g. if 1 -> 2, return 2)
        # If head is empty, it will just return head (head = None)
        if head is None or head.next is None:
            return head

        newHead = self.reverseList(head.next) # RECURSIVE CALL with the next node as head
        # Reverse the link (make the next pointer of next node point back)
        head.next.next = head 
        # As far as this recursive call now, the current head is the last node.
        head.next = None

        # newHead is a way to bring the first noded all the way back to the top
        return newHead        
        