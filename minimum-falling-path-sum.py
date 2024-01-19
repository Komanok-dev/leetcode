class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        if len(matrix) == 1:
            return min(matrix[0])
        dp = []
        for row in reversed(matrix):
            if not dp:
                dp = matrix[-1]
                continue
            temp = [0] * len(matrix)
            for i in range(len(row)):
                first = dp[i-1] if i > 0 else float('inf')
                last = dp[i+1] if i < len(row) - 1 else float('inf')
                temp[i] = min(first, dp[i], last) + row[i]
            dp = temp
        return min(dp)
