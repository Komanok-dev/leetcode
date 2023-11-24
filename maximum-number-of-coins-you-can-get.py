class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        result = 0
        right = len(piles) - 1
        piles.sort()
        while right > len(piles) / 3:
            result += piles[right-1]
            right -= 2
        return result
