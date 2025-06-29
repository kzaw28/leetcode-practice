# Last updated: 6/29/2025, 1:57:20 PM
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # Conversion ------------------------------
        h1, m1 = map(int, current.split(":"))
        currMins = h1 * 60 + m1

        h2, m2 = map(int, correct.split(":"))
        correctMins = h2 * 60 + m2

        # Subtracting -----------------------------
        ops = [60, 15, 5, 1] # Mins I can use
        res = 0
        diff = correctMins - currMins

        for op in ops:
            res += diff // op
            diff %= op
        
        return res