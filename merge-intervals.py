class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        for interval in intervals:
            if not ans or ans[-1][-1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][-1] = max(ans[-1][-1], interval[1])
