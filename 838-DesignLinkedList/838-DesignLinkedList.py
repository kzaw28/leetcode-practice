# Last updated: 5/27/2025, 6:45:51 PM
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        # Sentinel nodes
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def get(self, index: int) -> int:
        cur = self.head.next
        if index < 0 or index >= self.size:
            return -1
    
        for _ in range(index):
            cur = cur.next

        return cur.value

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.head.next, self.head
        # Change existing pointers
        next.prev = node
        prev.next = node

        # New node's pointer
        node.next = next
        node.prev = prev

        self.size += 1
        return
        

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.tail, self.tail.prev
        # Change existing pointers
        next.prev = node
        prev.next = node

        # New node's pointer
        node.next = next
        node.prev = prev

        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        cur = self.head.next # Initial index pointer
        for _ in range(index):
            cur = cur.next  # our pointer will end AT the index

        node, next, prev = ListNode(val), cur, cur.prev
        # Change existing pointers
        next.prev = node
        prev.next = node

        # New node's pointer
        node.next = next
        node.prev = prev

        self.size += 1
        return


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        cur = self.head.next # Initial index pointer
        for _ in range(index):
            cur = cur.next  # our pointer will end AT the index

        next, prev = cur.next, cur.prev
        # Change existing pointers
        next.prev = prev
        prev.next = next

        self.size -= 1
        return

# NOTES
# get and deleteAtIndex: The index must be within the range of existing nodes.

# addAtIndex: The index can be one past the last valid index to allow inserting a new node at the end of the list.

# Testing
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# print(obj.get(1)) # Expected: 2
# obj.deleteAtIndex(1)
# print(obj.get(1)) # Expected: 3
