class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        max_range = [0] * (n + 1)
        for i, range in enumerate(ranges):
            start, end = max(i - range, 0), min(i+range, n)
            max_range[start] = max(max_range[start], end - start)
        current_area, max_area, taps = 0, 0, 0
        for i, length in enumerate(max_range):
            if i > max_area:
                return -1
            if i > current_area:
                current_area = max_area
                taps += 1
            max_area = max(max_area, i + length)
        return taps
