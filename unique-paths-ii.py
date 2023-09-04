class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp = [0] * len(obstacleGrid[0])
        dp[0] = 1
        for m in obstacleGrid:
            if m[0] == 1:
                dp[0] = 0
            for i in range(len(m)):
                if m[i] == 1:
                    dp[i] = 0
                elif i > 0:
                    dp[i] += dp[i-1]
        return dp[-1]
