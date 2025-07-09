# Last updated: 7/8/2025, 9:09:21 PM
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

            # Move the pointers if..
            # diff1 = abs(height[left] - height[right - 1])
            # diff2 = abs(height[right] - height[left + 1])

            # if diff1 >= diff2:
            if height[left] < height[right]:
                left += 1
                # if height[left + 1] == height[right - 1]:
                #     if height[left] > height[right]:
                #         right -= 1
                #     else:
                #         left += 1
            else:
                right -= 1
        return res
