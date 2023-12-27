class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 +7
        dp = [[0 for _ in range(target+1)] for _ in range(2)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i % 2] = [0 for _ in range(target+1)]
            for v in range(1, k + 1):
                for j in range(v, target + 1):
                    dp[i % 2][j] = (dp[i % 2][j] + dp[(i - 1) % 2][j - v]) % MOD
        return dp[n % 2][target] % MOD
