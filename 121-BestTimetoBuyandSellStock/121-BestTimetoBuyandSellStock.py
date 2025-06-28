# Last updated: 6/28/2025, 6:51:19 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # update the lowest price so far
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit