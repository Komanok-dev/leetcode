from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        for i in range(len(arr)):
            dp[arr[i]] = 1
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in dp:
                    dp[arr[i]] += dp[arr[j]] * dp[arr[i] // arr[j]]
                    dp[arr[i]] %= MOD
        return sum(dp.values()) % MOD

    def numFactoredBinaryTrees2(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = defaultdict(int)
        for a in arr:
            count = 1
            for b in arr:
                if b > a:
                    break
                count += (dp[b] * dp[a/b])
            dp[a] = count
        return sum(dp.values()) % MOD
