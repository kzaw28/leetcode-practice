# Last updated: 7/12/2025, 12:02:48 PM
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Make the dictionary -----------
        lastOcc = {}
        for i, c in enumerate(s):
            lastOcc[c] = i

        # Partition ---------------------
        res = []
        curr = 0
        l = 0
        maxEnd = 0

        for i, c in enumerate(s):
            maxEnd = max(lastOcc[c], maxEnd)

            if i == maxEnd:
                res.append(maxEnd + 1 - l)
                l = maxEnd + 1

        return res

