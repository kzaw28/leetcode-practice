# Last updated: 6/29/2025, 3:43:59 PM
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # n => dimension of the current grid
        # r, c => the starting coordinates
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
              for j in range(n):
                # Check if the current pos is equal to the next pos
                if grid[r][c] != grid[r+i][c+j]:
                    allSame = False
                    break
            
            # Base case
            if allSame:
                return Node(grid[r][c], True)

            # Recursion ----------------------------
            n = n // 2

            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)

            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)