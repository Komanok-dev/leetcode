class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def length(cnt):
            l = 2 if cnt >= 2 else 1
            while cnt >= 10:
                l += 1
                cnt //= 10
            return l

        dp = [[len(s)] * (k + 1) for _ in range(len(s) + 1)]
        dp[0][0] = 0
        for i in range(1, len(s) + 1):
            for j in range(k + 1):
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                keep = delete = 0
                for y in range(i, len(s) + 1):
                    if s[i-1] == s[y-1]:
                        keep += 1
                    else:
                        delete += 1
                    if j + delete <= k:
                        dp[y][j+delete] = min(dp[y][j+delete], dp[i-1][j] + length(keep))
        return dp[len(s)][k]
