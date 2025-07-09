# Last updated: 7/8/2025, 9:10:29 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0

        while left != right:
            # Calculate the area
            w = right - left
            h = min(height[right], height[left])
            area = w * h
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
