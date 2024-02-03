class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        W = k + 1
        dp = [0] * W
        for i in range(len(arr)):
            curr_max = 0
            for j in range(1, min(k, i + 1) + 1):
                curr_max = max(curr_max, arr[i - j + 1])
                dp[i % W] = max(dp[i % W], (dp[(i - j) % W] if i >= j else 0) + curr_max * j)
        return dp[(len(arr) - 1) % W]
