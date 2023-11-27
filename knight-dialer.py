class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0],
                 [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        dp = [[1 for _ in range(10)] for _ in range(2)]
        print(dp)
        for i in range(n - 1):
            dp[(i+1) % 2] = [0] * 10
            for j in range(10):
                for num in moves[j]:
                    dp[(i+1) % 2][num] += dp[i % 2][j]
                    dp[(i+1) % 2][num] %= MOD
        return sum(dp[(n-1) % 2]) % MOD
