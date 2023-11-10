class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result1 = result2 = 0
        lowest1 = lowest2 = prices[0]
        for price in prices:
            lowest1 = min(lowest1, price)
            result1 = max(result1, price - lowest1)
            lowest2 = min(lowest2, price - result1)
            result2 = max(result2, price - lowest2)
        return result2
 