# Last updated: 6/5/2025, 10:29:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        myTree = []
        queue = deque()
        if root is None:
            return myTree
        queue.append(root)

        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == length - 1:
                    myTree.append(node.val)

        return myTree
        