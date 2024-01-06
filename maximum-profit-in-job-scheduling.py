import bisect


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        dp = [(0, 0)]
        for e, s, p in jobs:
            i = bisect.bisect_right(dp, (s + 1, 0)) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append((e, dp[i][1] + p))
        return dp[-1][1]
