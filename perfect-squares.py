class Solution:
    def numSquares(self, n: int) -> int:
        result = [0]
        while len(result) <= n:
            result += min(result[-i * i] for i in range(1, int(len(result) ** 0.5 + 1))) + 1,
        return result[n]
