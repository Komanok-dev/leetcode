class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[], [1, 1, 1, 1, 1]]
        a, e, i, o, u = 0, 1, 2, 3, 4 
        for j in range(2, n + 1):
            dp.append([0, 0, 0, 0, 0])
            dp[j][a] = (dp[j-1][e] + dp[j-1][i] + dp[j-1][u]) % MOD
            dp[j][e] = (dp[j-1][a] + dp[j-1][i]) % MOD
            dp[j][i] = (dp[j-1][e] + dp[j-1][o]) % MOD
            dp[j][o] = dp[j-1][i]
            dp[j][u] = (dp[j-1][i] + dp[j-1][o]) % MOD
        return sum(dp[n]) % MOD
