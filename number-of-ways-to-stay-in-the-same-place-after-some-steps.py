class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = int(10**9 + 7)
        lenght = min(1 + steps // 2, arrLen)
        dp = [0] * (lenght + 2)
        dp[1] = 1
        while steps > 0:
            steps -= 1
            dp2 = [0] * (lenght + 2)
            for i in range(1, lenght + 1):
                dp2[i] = (dp[i] + dp[i-1] + dp[i+1]) % MOD
            dp = dp2
        return dp[1]
