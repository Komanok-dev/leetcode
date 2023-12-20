class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()
        result = money - (prices[0] + prices[1])
        return result if result >= 0 else money
