class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            result = max(result, price - lowest)
        return result

    def maxProfit2(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        min_price, max_price, diff = prices[0], prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                max_price = prices[i]
            else:
                max_price = prices[i]
            if max_price - min_price > diff:
                diff = max_price - min_price
        return diff
