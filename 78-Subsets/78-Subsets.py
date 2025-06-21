# Last updated: 6/20/2025, 9:41:58 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        curr: List[int] = []
        i = 0


        def backtrack(res, curr, nums, i):
            if i >= len(nums):
                res.append(curr.copy())
                return

            # Left Tree
            curr.append(nums[i])
            backtrack(res, curr, nums, i+1)

            # Right Tree
            curr.pop()
            backtrack(res, curr, nums, i+1)

            
        backtrack(res, curr, nums, i)
        return res
        