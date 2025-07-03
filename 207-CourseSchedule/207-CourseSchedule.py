# Last updated: 7/3/2025, 12:51:57 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = deque([root])
        while queue:
            size = len(queue) # size of q changes dynamically

            for _ in range(size):
                curr = queue.popleft()
                curr.left, curr.right = curr.right, curr.left

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)


        return root 

            

            

            
