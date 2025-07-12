# Last updated: 7/12/2025, 12:54:49 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bucket Sort ------------
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
    
        j = 0

        for i in range(len(nums)):
            while count[j] == 0:
                j += 1
            nums[i] = j
            count[j] -= 1



