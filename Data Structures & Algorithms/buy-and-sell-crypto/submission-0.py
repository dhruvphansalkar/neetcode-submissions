class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        right_max = 0
        sol = 0
        for i, price in enumerate(prices):
            right_max = max(prices[n-i-1], right_max)
            sol = max(sol, right_max - prices[n-i-1])
        return sol     