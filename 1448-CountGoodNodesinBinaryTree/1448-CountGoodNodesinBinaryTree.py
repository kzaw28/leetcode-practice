# Last updated: 6/16/2025, 9:00:12 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            # Base Case -----
            if not node:
                return 0

            maxVal = max(maxVal, node.val)
            if node.val >= maxVal:
                count = 1   
            else:
                count = 0

            count += dfs(node.left, maxVal) 
            count += dfs(node.right, maxVal)

            return count

        return dfs(root, root.val)