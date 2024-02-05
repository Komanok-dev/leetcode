class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(2)]
        for moves in range(maxMove):
            for i in range(m):
                for j in range(n):
                    dp[(moves + 1) % 2][i][j] = (
                        ((1 if (i == 0) else dp[moves % 2][i - 1][j]) + \
                        (1 if (i == m - 1) else dp[moves % 2][i + 1][j])) % MOD + \
                        ((1 if (j == 0) else dp[moves % 2][i][j - 1]) + \
                        (1 if (j == n - 1) else dp[moves % 2][i][j + 1])) % MOD
                    ) % MOD
        return dp[maxMove % 2][startRow][startColumn]
