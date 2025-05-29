# Last updated: 5/29/2025, 5:36:03 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count unique values 'nums' --------------
        count = {}
        for n in nums:
            # Increment whatever value we have in n key (or 0 if not)
            count[n] = 1 + count.get(n, 0) 
        
        # Frequency Array -------------------------
        freq = [[] for i in range(len(nums) + 1)] # Populate the empty array
        for v, c in count.items():
            freq[c].append(v)

        # Find the k most frequent -----------------
        res = []
        for i in range(len(freq) -1, 0, -1):
            # Now you need loop to get in the inner arrays
            for j in freq[i]:
                res.append(j)
            # STOP if reaches k times
            if len(res) == k:
                return res


        return res


        
