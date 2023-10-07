class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(2)]
        prefix_dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(2)]
        for i in range(1, m+1):
            dp[1][i][1] = 1
            prefix_dp[1][i][1] = (prefix_dp[1][i-1][1] + dp[1][i][1])%MOD
        for l in range(2, n+1):
            for i in range(1, m+1):
                for j in range(1, k+1):
                    dp[l%2][i][j] = (i*dp[(l-1)%2][i][j]%MOD + prefix_dp[(l-1)%2][i-1][j-1])%MOD
                    prefix_dp[l%2][i][j] = (prefix_dp[l%2][i-1][j] + dp[l%2][i][j])%MOD
        print(dp)
        print(prefix_dp)
        return prefix_dp[n%2][m][k]
