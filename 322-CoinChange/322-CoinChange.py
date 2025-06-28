# Last updated: 6/28/2025, 6:13:26 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Use Bottom Up Approach
        dp = [float("inf")] * (amount + 1)
        # Each index is an amount
        # Each value at index is the number of coins needed to make up to that amount (or index number)
        dp[0] = 0 # Base Case

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)


        return dp[amount] if dp[amount] != float("inf") else -1