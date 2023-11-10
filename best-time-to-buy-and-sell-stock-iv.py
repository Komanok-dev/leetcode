class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        dp = [0] * len(prices)
        for _ in range(k):
            curr = -prices[0]
            profit = 0
            for i in range(1, len(prices)):
                curr = max(curr, dp[i] - prices[i])
                profit = max(profit, curr + prices[i])
                dp[i] = profit
        return profit
