# Last updated: 6/28/2025, 1:58:10 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        myMax = nums[0]
        mySum = 0

        for i in range(len(nums)):
            newSum = mySum + nums[i]
            mySum = max(nums[i], newSum)
            myMax = max(mySum, myMax)

        return myMax