# Last updated: 6/28/2025, 10:25:55 PM
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = deque()
        maxQ = deque()

        l = 0
        res = 0

        # MaxQ should store the max number (in decreasing) order
        # for the current sliding window
        for r in range(len(nums)):
            while maxQ and nums[r] > maxQ[-1]:
                maxQ.pop()
            maxQ.append(nums[r])

            while minQ and nums[r] < minQ[-1]:
                minQ.pop()
            minQ.append(nums[r])

            # Move the left (shrink) --------------------
            if maxQ[0] - minQ[0] > limit:
                if maxQ[0] == nums[l]:
                    maxQ.popleft()
                if minQ[0] == nums[l]:
                    minQ.popleft()
                l += 1
                
            res = max(res, r - l + 1)
        return res