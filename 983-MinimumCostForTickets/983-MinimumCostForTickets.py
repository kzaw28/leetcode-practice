# Last updated: 6/29/2025, 3:04:12 PM
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        daySet = set(days)
        lastDay = days[-1]
        dp = [0] * (lastDay + 1)

        for i in range(1, lastDay + 1):
            if i not in daySet:
                dp[i] = dp[i - 1]
            else:
                dp[i] =  min(
                    dp[max(0, i - 1)] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2]
                )

        return dp[lastDay]
