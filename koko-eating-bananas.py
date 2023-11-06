class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for i in piles:
                hours += (i - 1) // k + 1
            if hours <= h:
                result = min(result, k)
                right = k - 1
            else:
                left = k + 1
        return result
