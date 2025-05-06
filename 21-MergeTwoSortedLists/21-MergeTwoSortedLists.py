# Last updated: 5/6/2025, 2:54:45 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if (list1.val < list2.val):
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next # Update current pointer

        # if anyone of them is null, just append everything
        current.next = list1 or list2

        return dummy.next

        