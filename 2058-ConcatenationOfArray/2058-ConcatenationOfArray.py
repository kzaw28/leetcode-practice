# Last updated: 5/27/2025, 6:45:54 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        ans = [0] * (numsLength * 2) 
        for index in range(numsLength):
            ans[index] = nums[index]
            ans[index + numsLength] = nums[index]
        return ans