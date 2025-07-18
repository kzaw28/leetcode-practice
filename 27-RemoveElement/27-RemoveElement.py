# Last updated: 5/27/2025, 6:45:56 PM
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l 
        